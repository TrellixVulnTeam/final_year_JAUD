n  y |  j | � \ } } Wn] |  j k
 rc } |  j d | | f � � n/ |  j k
 r� } |  j d | | f � � n X| d k r� |  j  �  n  | d k r� |  j d | | | f � � n  | | f S(   NR   s   command: %s => %sR�   s   %s command error: %s %s(   R�   t   _get_tagged_responseR3   R0   (   RX   R}   R�   R[   Rr   R�   (    (    s   /usr/lib/python2.7/imaplib.pyt   _command_complete�  s    c         C   s�  |  j  �  } |  j |  j | � r� |  j j d � } | |  j k rX |  j d | � � n  |  j j d � } |  j j d � } | | g f |  j | <nwd  } |  j t | � s� |  j t	 | � r� |  j j d � } q� n  |  j d  k r'|  j t
 | � r|  j j d � |  _ d  S|  j d | � � n  |  j j d � } |  j j d � } | d  k r`d } n  | rw| d | } n  x� |  j t | � r�t |  j j d	 � � } |  j d
 k r�|  j d | � n  |  j | � } |  j | | | f � |  j  �  } qzW|  j | | � | d k rU|  j t | � rU|  j |  j j d � |  j j d � � n  |  j d k r�| d k r�|  j d | | f � n  | S(   NR�   s   unexpected tagged response: %sR�   Rr   t   data2s   unexpected response: '%s'R5   R�   Rl   i   s   read literal size %sR7   R�   R�   i   R�   s   %s response: %s(   R7   R�   R�   (   R�   R�   R�   (   t	   _get_linet   _matchRI   t   mot   groupR=   R3   R;   t   Untagged_responset   Untagged_statust   ContinuationR?   t   Literalt   intR9   RM   Rk   R�   t   Response_code(   RX   t   respR�   R[   R\   t   dat2Rl   Rr   (    (    s   /usr/lib/python2.7/imaplib.pyRO   �  sH     	 +c         C   s�   x{ |  j  | } | d  k	 r* |  j  | =| S|  j �  y |  j �  Wq |  j k
 ry } |  j d k rs |  j �  n  �  q Xq Wd  S(   Ni   (   R=   R;   R�   RO   R3   R9   t	   print_log(   RX   R�   t   resultR�   (    (    s   /usr/lib/python2.7/imaplib.pyR�   �  s    

c         C   s�   |  j  �  } | s$ |  j d � � n  | j d � sE |  j d � � n  | d  } |  j d k rr |  j d | � n |  j d | � | S(   Ns   socket error: EOFs   
s   socket error: unterminated linei����i   s   < %s(   Rm   R3   t   endswithR9   RM   R�   (   RX   Rp   (    (    s   /usr/lib/python2.7/imaplib.pyR�     s    
c         C   sc   | j  | � |  _ |  j d  k	 rV |  j d k rV |  j d | j |  j j �  f � n  |  j d  k	 S(   Ni   s   	matched r'%s' => %r(   t   matchR�   R;   R9   RM   R�   t   groups(   RX   t   cret   s(    (    s   /usr/lib/python2.7/imaplib.pyR�     s    &c         C   s7   d |  j  |  j f } |  j d |  _ d  |  j | <| S(   Ns   %s%si   (   RF   RB   R;   R=   (   RX   R�   (    (    s   /usr/lib/python2.7/imaplib.pyR�      s    c         C   s�   t  | � t  d � k	 r | St | � d k rR | d | d f d d	 f k rR | S| rt |  j j | � d  k rt | S|  j | � S(
   NR5   i   i    i����R�   R�   t   "(   R�   R�   (   R  R  (   R�   Ro   t	   mustquoteR�   R;   R�   (   RX   R�   (    (    s   /usr/lib/python2.7/imaplib.pyR�   (  s    2c         C   s,   | j  d d � } | j  d d � } d | S(   Ns   \s   \\R  s   \"s   "%s"(   t   replace(   RX   R�   (    (    s   /usr/lib/python2.7/imaplib.pyR�   6  s    c         G   s   |  j  | |  j | | � � S(   N(   R�   R�   (   RX   R}   R�   (    (    s   /usr/lib/python2.7/imaplib.pyR�   >  s    c         C   sw   | d k r | | f S| |  j  k r2 | d  g f S|  j  j | � } |  j d k rm |  j d | | f � n  | | f S(   NR�   i   s   untagged_responses[%s] => %s(   R>   R;   t   popR9   RM   (   RX   R[   R\   R}   Rr   (    (    s   /usr/lib/python2.7/imaplib.pyR{   C  s    
c         C   sl   | d  k r t j �  } n  t j d t j | � � } t j j d | | d d | f � t j j �  d  S(   Ns   %M:%Ss     %s.%02d %s
id   (   R;   t   timet   strftimet	   localtimeR�   t   stderrt   writet   flush(   RX   R  t   secst   tm(    (    s   /usr/lib/python2.7/imaplib.pyRM   R  s
    %c         C   sR   | j  �  } | s d  Sd } t d �  | � } |  j d | | j | � f � d  S(   Ns   
		c         S   s3   d |  d |  d d r+ d j  |  d � p. d f S(   Ns   %s: "%s"i    i   s   " "R5   (   R�   (   t   x(    (    s   /usr/lib/python2.7/imaplib.pyt   <lambda>^  s    s   untagged responses dump:%s%s(   t   itemst   mapRM   R�   (   RX   t   dictt   lt   t(    (    s   /usr/lib/python2.7/imaplib.pyR�   Y  s     c         C   sM   | t  j  �  f |  j |  j <|  j d 7_ |  j |  j k rI d |  _ n  d  S(   Ni   i    (   R  RL   RK   RJ   (   RX   Rp   (    (    s   /usr/lib/python2.7/imaplib.pyR�   a  s    c         C   s�   |  j  d t |  j � � |  j |  j } } xX | r� y |  j  |  j | �  Wn n X| d 7} | |  j k rz d } n  | d 8} q0 Wd  S(   Ns   last %d IMAP4 interactions:i   i    (   RM   Ro   RL   RK   RJ   (   RX   t   it   n(    (    s   /usr/lib/python2.7/imaplib.pyR  h  s    	
	N(P   R1   R2   t   __doc__t	   ExceptionR0   R3   R4   RG   RH   R  t
   IMAP4_PORTR^   Rd   RC   Rk   Rm   Rs   Ru   Rf   R~   R�   R�   R�   RQ   R�   Rt   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R|   R�   R�   R�   R�   R@   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   RO   R�   R�   R�   R�   R�   R�   R�   R{   R;   RM   R�   R�   R  (    (    (    s   /usr/lib/python2.7/imaplib.pyR    m   s�   ,;																																
					 									
						J		L										t	   IMAP4_SSLc           B   sh   e  Z d  Z d e d
 d
 d � Z d e d � Z d �  Z d �  Z d �  Z	 d �  Z
 d �  Z d	 �  Z RS(   s�  IMAP4 client class over SSL connection

        Instantiate with: IMAP4_SSL([host[, port[, keyfile[, certfile]]]])

                host - host's name (default: localhost);
                port - port number (default: standard IMAP4 SSL port).
                keyfile - PEM formatted file that contains your private key (default: None);
                certfile - PEM formatted certificate chain file (default: None);

        for more documentation see the docstring of the parent class IMAP4.
        R5   c         C   s)   | |  _  | |  _ t j |  | | � d  S(   N(   t   keyfilet   certfileR    R^   (   RX   RY   RZ   R%  R&  (    (    s   /usr/lib/python2.7/imaplib.pyR^   �  s    		c         C   sd   | |  _  | |  _ t j | | f � |  _ t j |  j |  j |  j � |  _	 |  j	 j
 d � |  _ d S(   s�   Setup connection to remote server on "host:port".
                (default: localhost:standard IMAP4 SSL port).
            This connection will be used by the routines:
                read, readline, send, shutdown.
            Re   N(   RY   RZ   Rf   Rg   Rh   t   sslt   wrap_socketR%  R&  t   sslobjRi   Rj   (   RX   RY   RZ   (    (    s   /usr/lib/python2.7/imaplib.pyRC   �  s
    		!c         C   s   |  j  j | � S(   s   Read 'size' bytes from remote.(   Rj   Rk   (   RX   Rl   (    (    s   /usr/lib/python2.7/imaplib.pyRk   �  s    c         C   s   |  j  j �  S(   s   Read line from remote.(   Rj   Rm   (   RX   (    (    s   /usr/lib/python2.7/imaplib.pyRm   �  s    c         C   sY   t  | � } xF | d k rT |  j j | � } | | k r= Pn  | | } | | } q Wd S(   s   Send data to remote.i    N(   Ro   R)  R  (   RX   Rr   t   bytest   sent(    (    s   /usr/lib/python2.7/imaplib.pyRs   �  s    
c         C   s   |  j  j �  |  j j �  d S(   s    Close I/O established in "open".N(   Rj   Rt   Rh   (   RX   (    (    s   /usr/lib/python2.7/imaplib.pyRu   �  s    c         C   s   |  j  S(   sn   Return socket instance used to connect to IMAP4 server.

            socket = <instance>.socket()
            (   Rh   (   RX   (    (    s   /usr/lib/python2.7/imaplib.pyRf   �  s    c         C   s   |  j  S(   s�   Return SSLObject instance used to communicate with the IMAP4 server.

            ssl = ssl.wrap_socket(<instance>.socket)
            (   R)  (   RX   (    (    s   /usr/lib/python2.7/imaplib.pyR'  �  s    N(   R1   R2   R!  t   IMAP4_SSL_PORTR;   R^   RC   Rk   Rm   Rs   Ru   Rf   R'  (    (    (    s   /usr/lib/python2.7/imaplib.pyR$  |  s   					c           B   sJ   e  Z d  Z d �  Z d d d � Z d �  Z d �  Z d �  Z d �  Z	 RS(   s�   IMAP4 client class over a stream

    Instantiate with: IMAP4_stream(command)

            where "command" is a string that can be pas