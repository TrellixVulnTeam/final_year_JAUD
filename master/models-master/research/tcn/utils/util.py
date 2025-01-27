       """Exhaust the stream.  This consumes all the data left until the
        limit is reached.

        :param chunk_size: the size for a chunk.  It will read the chunk
                           until the stream is exhausted and throw away
                           the results.
        """
        to_read = self.limit - self._pos
        chunk = chunk_size
        while to_read > 0:
            chunk = min(to_read, chunk)
            self.read(chunk)
            to_read -= chunk

    def read(self, size=None):
        """Read `size` bytes or if size is not provided everything is read.

        :param size: the number of bytes read.
        """
        if self._pos >= self.limit:
            return self.on_exhausted()
        if size is None or size == -1:  # -1 is for consistence with file
            size = self.limit
        to_read = min(self.limit - self._pos, size)
        try:
            read = self._read(to_read)
        except (IOError, ValueError):
            return self.on_disconnect()
        if to_read and len(read) != to_read:
            return self.on_disconnect()
        self._pos += len(read)
        return read

    def readline(self, size=None):
        """Reads one line from the stream."""
        if self._pos >= self.limit:
            return self.on_exhausted()
        if size is None:
            size = self.limit - self._pos
        else:
            size = min(size, self.limit - self._pos)
        try:
            line = self._readline(size)
        except (ValueError, IOError):
            return self.on_disconnect()
        if size and not line:
            return self.on_disconnect()
        self._pos += len(line)
        return line

    def readlines(self, size=None):
        """Reads a file into a list of strings.  It calls :meth:`readline`
        until the file is read to the end.  It does support the optional
        `size` argument if the underlaying stream supports it for
        `readline`.
        """
        last_pos = self._pos
        result = []
        if size is not None:
            end = min(self.limit, last_pos + size)
        else:
            end = self.limit
        while 1:
            if size is not None:
                size -= last_pos - self._pos
            if self._pos >= end:
                break
            result.append(self.readline(size))
            if size is not None:
                last_pos = self._pos
        return result

    def tell(self):
        """Returns the position of the stream.

        .. versionadded:: 0.9
        """
        return self._pos

    def __next__(self):
        line = self.readline()
        if not line:
            raise StopIteration()
        return line
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
��fX  �               @   s�   d  Z  d d l Z d d l Z d d l Z e j j d � pH d e j k Z d d �  Z Gd d �  d e e	 � Z
 d	 a d
 d �  Z d S)z�
    werkzeug.filesystem
    ~~~~~~~~~~~~~~~~~~~

    Various utilities for the local filesystem.

    :copyright: (c) 2015 by the Werkzeug Team, see AUTHORS for more details.
    :license: BSD, see LICENSE for more details.
�    N�linuxZbsdc             C   sG   |  d k r d Sy t  j |  � j d k SWn t k
 rB d SYn Xd S)z�
    Given an encoding this figures out if the encoding is actually ASCII (which
    is something we don't actually want in most cases). This is necessary
    because ASCII comes under many names such as ANSI_X3.4-1968.
    NF�ascii)�codecs�lookup�name�LookupError)�encoding� r	   �5/usr/lib/python3/dist-packages/werkzeug/filesystem.py�_is_ascii_encoding   s    r   c               @   s   e  Z d  Z d Z d S)�BrokenFilesystemWarningzcThe warning used by Werkzeug to signal a broken filesystem. Will only be
    used once per runtime.N)�__name__�
__module__�__qualname__�__doc__r	   r	   r	   r
   r   #   s   r   Fc              C   sR   t  j �  }  t r |  s% t |  � rN t sJ t j d j |  � t � d a d S|  S)a	  
    Returns the filesystem encoding that should be used. Note that this is
    different from the Python understanding of the filesystem encoding which
    might be deeply flawed. Do not use this value against Python's unicode APIs
    because it might be different. See :ref:`filesystem-encoding` for the exact
    behavior.

    The concept of a filesystem encoding in generally is not something you
    should rely on. As such if you ever need to use this function except for
    writing wrapper code reconsider.
    z`Detected a misconfigured UNIX filesystem: Will use UTF-8 as filesystem encoding instead of {0!r}Tzutf-8)	�sys�getfilesystemencoding�#has_likely_buggy_unicode_filesystemr   �!_warned_about_filesystem_encoding�warnings�warn�formatr   )�rvr	   r	   r
   �get_filesystem_encoding+   s    r   )r   r   r   r   �platform�
startswithr   r   �RuntimeWarning�UnicodeWarningr   r   r   r	   r	   r	   r
   �<module>
   s   !                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
��fX  �            2   @   s�  d  Z  d d l m Z d d l Z d d l m Z d Z d