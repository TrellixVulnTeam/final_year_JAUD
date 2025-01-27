  s   e  Z d  Z d d � Z RS(   s7   Ttk Label widget displays a textual label and/or image.Nc         K  s   t  � |  | d | � d S(   sG  Construct a Ttk Label with parent master.

        STANDARD OPTIONS

            class, compound, cursor, image, style, takefocus, text,
            textvariable, underline, width

        WIDGET-SPECIFIC OPTIONS

            anchor, background, font, foreground, justify, padding,
            relief, text, wraplength
        s
   ttk::labelN(   R�   R�   (   R�   R%   RG   (    (    R'   R�   �  s    (   R�   R�   R�   R�   (    (    (    R'   R   �  s   c             s   e  Z d  Z d d � Z RS(   s�   Ttk Labelframe widget is a container used to group other widgets
    together. It has an optional label, which may be a plain text string
    or another widget.Nc         K  s   t  � |  | d | � d S(   s�   Construct a Ttk Labelframe with parent master.

        STANDARD OPTIONS

            class, cursor, style, takefocus

        WIDGET-SPECIFIC OPTIONS
            labelanchor, text, underline, padding, labelwidget, width,
            height
        s   ttk::labelframeN(   R�   R�   (   R�   R%   RG   (    (    R'   R�   �  s    (   R�   R�   R�   R�   (    (    (    R'   R   �  s   c             s   e  Z d  Z d d � Z RS(   sb   Ttk Menubutton widget displays a textual label and/or image, and
    displays a menu when pressed.Nc         K  s   t  � |  | d | � d S(   s  Construct a Ttk Menubutton with parent master.

        STANDARD OPTIONS

            class, compound, cursor, image, state, style, takefocus,
            text, textvariable, underline, width

        WIDGET-SPECIFIC OPTIONS

            direction, menu
        s   ttk::menubuttonN(   R�   R�   (   R�   R%   RG   (    (    R'   R�     s    (   R�   R�   R�   R�   (    (    (    R'   R     s   c             sz   e  Z d  Z d d � Z d �  Z d �  Z d �  Z d �  Z d �  Z d �  Z	 d d	 � Z
 d d
 � Z d �  Z d �  Z RS(   s�   Ttk Notebook widget manages a collection of windows and displays
    a single one at a time. Each child window is associated with a tab,
    which the user may select to change the currently-displayed window.Nc         K  s   t  � |  | d | � d S(   s\  Construct a Ttk Notebook with parent master.

        STANDARD OPTIONS

            class, cursor, style, takefocus

        WIDGET-SPECIFIC OPTIONS

            height, padding, width

        TAB OPTIONS

            state, sticky, padding, text, image, compound, underline

        TAB IDENTIFIERS (tab_id)

            The tab_id argument found in several methods may take any of
            the following forms:

                * An integer between zero and the number of tabs
                * The name of a child window
                * A positional specification of the form "@x,y", which
                  defines the tab
                * The string "current", which identifies the
                  currently-selected tab
                * The string "end", which returns the number of tabs (only
                  valid for method index)
        s   ttk::notebookN(   R�   R�   (   R�   R%   RG   (    (    R'   R�   %  s    c         K  s&   |  j  j |  j d | t | � � d S(   s�   Adds a new tab to the notebook.

        If window is currently managed by the notebook but hidden, it is
        restored to its previous position.t   addN(   R!   Rx   R�   R5   (   R�   t   childRG   (    (    R'   R�   E  s    c         C  s   |  j  � |  j d | � d S(   sX   Removes the tab specified by tab_id, unmaps and unmanages the
        associated window.t   forgetN(   R!   Rx   R�   (   R�   t   tab_id(    (    R'   R�   M  s    c         C  s   |  j  � |  j d | � d S(   s�   Hides the tab specified by tab_id.

        The tab will not be displayed, but the associated window remains
        managed by the notebook and its configuration remembered. Hidden
        tabs may be restored with the add command.t   hideN(   R!   Rx   R�   (   R�   R�   (    (    R'   R�   S  s    c         C  s   |  j  � |  j d | | � S(   sZ   Returns the name of the tab element at position x, y, or the
        empty string if none.R�   (   R!   Rx   R�   (   R�   R�   R�   (    (    R'   R�   \  s    c         C  s%   |  j  � |  j  � |  j d | � � S(   s|   Returns the numeric index of the tab specified by tab_id, or
        the total number of tabs if tab_id is the string "end".R�   (   R!   R�   Rx   R�   (   R�   R�   (    (    R'   R�   b  s    c         K  s)   |  j  j |  j d | | t | � � d S(   s�   Inserts a pane at the specified position.

        pos is either the string end, an integer index, or the name of
        a managed child. If child is already managed by the notebook,
        moves it to the specified position.t   insertN(   R!   Rx   R�   R5   (   R�   t   posR�   RG   (    (    R'   R�   h  s    c         C  s   |  j  � |  j d | � S(   s�   Selects the specified tab.

        The associated child window will be displayed, and the
        previously-selected window (if different) is unmapped. If tab_id
        is omitted, returns the widget name of the currently selected
        pane.t   select(   R!   Rx   R�   (   R�   R�   (    (    R'   R�   q  s    c         K  s5   | d k	 r d | | <n  t  |  j | |  j d | � S(   s�   Query or modify the options of the specific tab_id.

        If kw is not given, returns a dict of the tab option values. If option
        is specified, returns the value of that option. Otherwise, sets the
        options to the corresponding values.Nt   tab(   R{   R!   R�   (   R�   R�   R�   RG   (    (    R'   R�   {  s    c         C  s(   |  j  � |  j  � |  j d � p$ d � S(   s2   Returns a list of windows managed by the notebook.t   tabs(    (   R!   Rq   Rx   R�   (   R�   (    (    R'   R�   �  s    c         C  s   |  j  � d |  j � d S(   s�  Enable keyboard traversal for a toplevel window containing
        this notebook.

        This will extend the bindings for the toplevel window containing
        this notebook as follows:

            Control-Tab: selects the tab following the currently selected
                         one

            Shift-Control-Tab: selects the tab preceding the currently
                               selected one

            Alt-K: where K is the mnemonic (underlined) character of any
                   tab, will select that tab.

        Multiple notebooks in a single toplevel may be enabled for
        traversal, including nested notebooks. However, notebook traversal
        only works properly if all panes are direct children of the
        notebook.s   ttk::notebook::enableTraversalN(   R!   Rx   R�   (   R�   (    (    R'   t   enable_traversal�  s    (   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   (    (    (    R'   R	      s    								
	c             sG   e  Z d  Z d d � Z e j j Z d �  Z d d � Z d d � Z	 RS(   sf   Ttk Panedwindow widget displays a number of subwindows, stacked
    either vertically or horizontally.Nc         K  s   t  � |  | d | � d S(   s�   Construct a Ttk Panedwindow with parent master.

        STANDARD OPTIONS

            class, cursor, style, takefocus

        WIDGET-SPECIFIC OPTIONS

            orient, width, height

        PANE OPTIONS

            weight
        s   ttk::panedwindowN(   R�   R�   (   R�   R%   RG   (    (    R'   R�   �  s    c         K  s)   |  j  j |  j d | | t | � � d S(   s�   Inserts a pane at the specified positions.

        pos is either the string end, and integer index, or the name
        of a child. If child is already managed by the paned window,
        moves it to the specified position.R�   N(   R!   Rx   R�   R5   (   R�   R�   R�   RG   (    (    R'   R�   �  s    c         K  s5   | d k	 r d | | <n  t  |  j | |  j d | � S(   sQ  Query or modify the options of the specified pane.

        pane is either an integer index or the name of a managed subwindow.
        If kw is not given, returns a dict of the pane option values. If
        option is specified then the value for that option is returned.
        Otherwise, sets the options to the corresponding values.Nt   pane(   R{   R!   R�   (   R�   R�   R�   RG   (    (    R'   R�   �  s    c         C  s(   |  j  � |  j  � |  j d | | � � S(   sL  If newpos is specified, sets the position of sash number index.

        May adjust the positions of adjacent sashes to ensure that
        positions are monotonically increasing. Sash positions are further
        constrained to be between 0 and the total size of the widget.

        Returns the new position of sash number index.t   sashpos(   R!   R