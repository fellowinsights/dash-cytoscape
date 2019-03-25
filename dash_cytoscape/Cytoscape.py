# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Cytoscape(Component):
    """A Cytoscape component.
A Component Library for Dash aimed at facilitating network visualization in
Python, wrapped around [Cytoscape.js](http://js.cytoscape.org/).

Keyword arguments:
- id (string; optional): The ID used to identify this component in Dash callbacks.
- className (string; optional): Sets the class name of the element (the value of an element's html
class attribute).
- style (dict; optional): Add inline styles to the root element.
- elements (list; optional): A list of dictionaries representing the elements of the networks.
    1. Each dictionary describes an element, and specifies its purpose.
        - `group` (string): Either 'nodes' or 'edges'. If not given, it's automatically inferred.
        - `data` (dictionary): Element specific data.
             - `id` (string): Reference to the element, useful for selectors and edges. Randomly assigned if not given.
             - `label` (string): Optional name for the element, useful when `data(label)` is given to a style's `content` or `label`. It is only a convention.
             - `parent` (string): Only for nodes. Optional reference to another node. Needed to create compound nodes.
             - `source` (string): Only for edges. The id of the source node, which is where the edge starts.
             - `target` (string): Only for edges. The id of the target node, where the edge ends.
        - `position` (dictionary): Only for nodes. The position of the node.
             - `x` (number): The x-coordinate of the node.
             - `y` (number): The y-coordinate of the node.
        - `selected` (boolean): If the element is selected upon initialisation.
        - `selectable` (boolean): If the element can be selected.
        - `locked` (boolean): Only for nodes. If the position is immutable.
        - `grabbable` (boolean): Only for nodes. If the node can be grabbed and moved by the user.
        - `classes` (string): Space separated string of class names of the element. Those classes can be selected by a style selector.

    2. The [official Cytoscape.js documentation](http://js.cytoscape.org/#notation/elements-json) offers an extensive overview and examples of element declaration.
- stylesheet (list; optional): A list of dictionaries representing the styles of the elements.
    1. Each dictionary requires the following keys:
        - `selector` (string): Which elements you are styling. Generally, you select a group of elements (node, edges, both), a class (that you declare in the element dictionary), or an element by ID.
        - `style` (dictionary): What aspects of the elements you want to modify. This could be the size or color of a node, the shape of an edge arrow, or many more.

    2. Both [the selector string](http://js.cytoscape.org/#selectors) and
    [the style dictionary](http://js.cytoscape.org/#style/node-body) are
    exhaustively documented in the Cytoscape.js docs. Although methods such
    as `cy.elements(...)` and `cy.filter(...)` are not available, the selector
    string syntax stays the same.
- layout (dict; optional): A dictionary specifying how to set the position of the elements in your
graph. The `'name'` key is required, and indicates which layout (algorithm) to
use.
    1. The layouts available by default are:
        - `random`: Randomly assigns positions
        - `preset`: Assigns position based on the `position` key in element dictionaries
        - `circle`: Single-level circle, with optional radius
        - `concentric`: Multi-level circle, with optional radius
        - `grid`: Square grid, optionally with numbers of `rows` and `cols`
        - `breadthfirst`: Tree structure built using BFS, with optional `roots`
        - `cose`: Force-directed physics simulation

    2. The keys accepted by `layout` vary depending on the algorithm, but some
    keys are accepted by all layouts:
        - `fit` (boolean): Whether to render the nodes in order to fit the canvas.
        - `padding` (number): Padding around the sides of the canvas, if fit is enabled.
        - `animate` (boolean): Whether to animate change in position when the layout changes.
        - `animationDuration` (number): Duration of animation in milliseconds, if enabled.
        - `boundingBox` (dictionary): How to constrain the layout in a specific area. Keys accepted are either `x1, y1, x2, y2` or `x1, y1, w, h`, all of which receive a pixel value.

    3. The complete list of layouts and their accepted options are available
    on the [Cytoscape.js docs](http://js.cytoscape.org/#layouts).
    Note that certain keys are not supported in Dash since the value is a
    JavaScript function or a callback. Please visit [this issue](https://github.com/plotly/dash-cytoscape/issues/25)
    for more information.
- pan (dict; optional): Dictionary indicating the initial panning position of the graph. The
following keys are accepted:
    - `x` (number): The x-coordinate of the position.
    - `y` (number): The y-coordinate of the position.
- zoom (number; optional): The initial zoom level of the graph. You can set `minZoom` and
`maxZoom` to set restrictions on the zoom level.
- panningEnabled (boolean; optional): Whether panning the graph is enabled (i.e., the position of the graph is
mutable overall).
- userPanningEnabled (boolean; optional): Whether user events (e.g. dragging the graph background) are allowed to
pan the graph.
- minZoom (number; optional): A minimum bound on the zoom level of the graph. The viewport can not be
scaled smaller than this zoom level.
- maxZoom (number; optional): A maximum bound on the zoom level of the graph. The viewport can not be
scaled larger than this zoom level.
- zoomingEnabled (boolean; optional): Whether zooming the graph is enabled (i.e., the zoom level of the graph
is mutable overall).
- userZoomingEnabled (boolean; optional): Whether user events (e.g. dragging the graph background) are allowed
to pan the graph.
- boxSelectionEnabled (boolean; optional): Whether box selection (i.e. drag a box overlay around, and release it
to select) is enabled. If enabled, the user must taphold to pan the graph.
- autoungrabify (boolean; optional): Whether nodes should be ungrabified (not grabbable by user) by
default (if true, overrides individual node state).
- autolock (boolean; optional): Whether nodes should be locked (not draggable at all) by default
(if true, overrides individual node state).
- autounselectify (boolean; optional): Whether nodes should be unselectified (immutable selection state) by
default (if true, overrides individual element state).
- autoRefreshLayout (boolean; optional): Whether the layout should be refreshed when elements are added or removed.
- tapNode (dict; optional): The complete node dictionary returned when you tap or click it.

    1. Node-specific items:
        - `edgesData` (dictionary)
        - `renderedPosition` (dictionary)
        - `timeStamp` (number)

    2. General items (for all elements):
        - `classes` (string)
        - `data` (dictionary)
        - `grabbable` (boolean)
        - `group` (string)
        - `locked` (boolean)
        - `position` (dictionary)
        - `selectable` (boolean)
        - `selected` (boolean)
        - `style` (dictionary)

    3. Items for compound nodes:
        - `ancestorsData` (dictionary)
        - `childrenData` (dictionary)
        - `descendantsData` (dictionary)
        - `parentData` (dictionary)
        - `siblingsData` (dictionary)
        - `isParent` (boolean)
        - `isChildless` (boolean)
        - `isChild` (boolean)
        - `isOrphan` (boolean)
        - `relativePosition` (dictionary)
- tapNodeData (dict; optional): The data dictionary of a node returned when you tap or click it.
- tapEdge (dict; optional): The complete edge dictionary returned when you tap or click it.

    1. Edge-specific items:
        - `isLoop` (boolean)
        - `isSimple` (boolean)
        - `midpoint` (dictionary)
        - `sourceData` (dictionary)
        - `sourceEndpoint` (dictionary)
        - `targetData` (dictionary)
        - `targetEndpoint` (dictionary)
        - `timeStamp` (number)

    2. General items (for all elements):
        - `classes` (string)
        - `data` (dictionary)
        - `grabbable` (boolean)
        - `group` (string)
        - `locked` (boolean)
        - `selectable` (boolean)
        - `selected` (boolean)
        - `style` (dictionary)
- tapEdgeData (dict; optional): The data dictionary of an edge returned when you tap or click it.
- mouseoverNodeData (dict; optional): The data dictionary of a node returned when you hover over it.
- mouseoverEdgeData (dict; optional): The data dictionary of an edge returned when you hover over it.
- selectedNodeData (list; optional): The list of data dictionaries of all selected nodes (e.g. using
Shift+Click to select multiple nodes, or Shift+Drag to use box selection).
- selectedEdgeData (list; optional): The list of data dictionaries of all selected edges (e.g. using
Shift+Click to select multiple nodes, or Shift+Drag to use box selection).
- operation (dict; optional): [Fellow] An invocation mechanism for customized, pre-defined operations
on the graph.

    1. Expected dictionary attributes:
    - `command` (string): Name of the operation
    - `timestamp` (string): Set a time later than the previous timestamp.
    The component will not re-apply an operation with a stale timestamp.
    - `args` (dictionary): Arguments required by the operation.

    2. Supported operations:
    - `locateNode`: Position and zoom the graph viewport over the element
    specified by the `selector` (and, therefore, allows for searching the
    graph).
        - Argument:
            - `selector`: The node to locate in Cytoscape selector syntax

    3. Limitations:
    - The operation happens before the Cytoscape element renders."""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, elements=Component.UNDEFINED, stylesheet=Component.UNDEFINED, layout=Component.UNDEFINED, pan=Component.UNDEFINED, zoom=Component.UNDEFINED, panningEnabled=Component.UNDEFINED, userPanningEnabled=Component.UNDEFINED, minZoom=Component.UNDEFINED, maxZoom=Component.UNDEFINED, zoomingEnabled=Component.UNDEFINED, userZoomingEnabled=Component.UNDEFINED, boxSelectionEnabled=Component.UNDEFINED, autoungrabify=Component.UNDEFINED, autolock=Component.UNDEFINED, autounselectify=Component.UNDEFINED, autoRefreshLayout=Component.UNDEFINED, tapNode=Component.UNDEFINED, tapNodeData=Component.UNDEFINED, tapEdge=Component.UNDEFINED, tapEdgeData=Component.UNDEFINED, mouseoverNodeData=Component.UNDEFINED, mouseoverEdgeData=Component.UNDEFINED, selectedNodeData=Component.UNDEFINED, selectedEdgeData=Component.UNDEFINED, operation=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'className', 'style', 'elements', 'stylesheet', 'layout', 'pan', 'zoom', 'panningEnabled', 'userPanningEnabled', 'minZoom', 'maxZoom', 'zoomingEnabled', 'userZoomingEnabled', 'boxSelectionEnabled', 'autoungrabify', 'autolock', 'autounselectify', 'autoRefreshLayout', 'tapNode', 'tapNodeData', 'tapEdge', 'tapEdgeData', 'mouseoverNodeData', 'mouseoverEdgeData', 'selectedNodeData', 'selectedEdgeData', 'operation']
        self._type = 'Cytoscape'
        self._namespace = 'dash_cytoscape'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'className', 'style', 'elements', 'stylesheet', 'layout', 'pan', 'zoom', 'panningEnabled', 'userPanningEnabled', 'minZoom', 'maxZoom', 'zoomingEnabled', 'userZoomingEnabled', 'boxSelectionEnabled', 'autoungrabify', 'autolock', 'autounselectify', 'autoRefreshLayout', 'tapNode', 'tapNodeData', 'tapEdge', 'tapEdgeData', 'mouseoverNodeData', 'mouseoverEdgeData', 'selectedNodeData', 'selectedEdgeData', 'operation']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Cytoscape, self).__init__(**args)
