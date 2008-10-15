from advene.model.cam.consts import BOOTSTRAP_URI, CAMSYS_TYPE
from advene.model.cam.exceptions import UnsafeUseWarning, SemanticError
from advene.model.cam.group import CamGroupMixin
from advene.model.cam.media import Media
from advene.model.cam.annotation import Annotation
from advene.model.cam.relation import Relation
from advene.model.cam.view import View
from advene.model.cam.resource import Resource
from advene.model.cam.tag import Tag
from advene.model.cam.list import List
from advene.model.cam.query import Query
from advene.model.cam.import_ import Import
import advene.model.cam.util.bookkeeping as bk
from advene.model.consts import DC_NS_PREFIX, RDFS_NS_PREFIX
from advene.model.core.package import Package as CorePackage
from advene.model.core.all_group import AllGroup as CoreAllGroup
from advene.model.core.own_group import OwnGroup as CoreOwnGroup

from warnings import warn
from weakref import ref as wref

class _AllGroup(CamGroupMixin, CoreAllGroup):

    def iter_tags(self):
        """
        This method is inherited from CoreAllGroup but is unsafe on
        cam.Package. Use instead `iter_user_tags`.
        """
        warn("use iter_user_tags instead", UnsafeUseWarning, 2)
        return super(_AllGroup, self).iter_tags()

    def _iter_tags_nowarn(self):
        """
        Allows to call iter_tags internally without raising a warning.
        """
        return super(_AllGroup, self).iter_tags()

    def iter_user_tags(self):
        o = self._owner
        meta = [(CAMSYS_TYPE, None, None)] 
        for be, pdict in o._backends_dict.items():
            for i in be.iter_tags(pdict, meta=meta):
                yield pdict[i[1]].get_element(i)

    def iter_annotation_types(self):
        o = self._owner
        meta = [(CAMSYS_TYPE, "annotation-type", False)]
        for be, pdict in o._backends_dict.items():
            for i in be.iter_tags(pdict, meta=meta):
                yield pdict[i[1]].get_element(i)

    def iter_relation_types(self):
        o = self._owner
        meta = [(CAMSYS_TYPE, "relation-type", False)] 
        for be, pdict in o._backends_dict.items():
            for i in be.iter_tags(pdict, meta=meta):
                yield pdict[i[1]].get_element(i)

    def iter_lists(self, item=None, position=None):
        """
        This method is inherited from CoreAllGroup but is unsafe on
        cam.Package. Use instead `iter_user_lists`.
        """
        warn("use iter_user_lists instead", UnsafeUseWarning, 2)
        return super(_AllGroup, self).iter_lists(item=item, position=position)

    def _iter_lists_nowarn(self, item=None, position=None):
        """
        Allows to call iter_lists internally without raising a warning.
        """
        return super(_AllGroup, self).iter_lists(item=item, position=position)

    def iter_user_lists(self):
        o = self._owner
        meta = [(CAMSYS_TYPE, None, None)] 
        for be, pdict in o._backends_dict.items():
            for i in be.iter_lists(pdict, meta=meta):
                yield pdict[i[1]].get_element(i)

    def iter_schemas(self):
        o = self._owner
        meta = [(CAMSYS_TYPE, "schema", False)] 
        for be, pdict in o._backends_dict.items():
            for i in be.iter_lists(pdict, meta=meta):
                yield pdict[i[1]].get_element(i)

    def count_tags(self):
        """
        This method is inherited from CoreAllGroup but is unsafe on
        cam.Package. Use instead `count_user_tags`.
        """
        warn("use count_user_tags instead", UnsafeUseWarning, 2)
        return super(_AllGroup, self).count_tags()

    def _count_tags_nowarn(self):
        """
        Allows to call count_tags internally without raising a warning.
        """
        return super(_AllGroup, self).count_tags()

    def count_user_tags(self):
        o = self._owner
        meta = [(CAMSYS_TYPE, None, None)] 
        return sum( be.count_tags(pdict, meta=meta)
                    for be, pdict in o._backends_dict.items() )

    def count_annotation_types(self):
        o = self._owner
        meta = [(CAMSYS_TYPE, "annotation-type", False)] 
        return sum( be.count_tags(pdict, meta=meta)
                    for be, pdict in o._backends_dict.items() )

    def count_relation_types(self):
        o = self._owner
        meta = [(CAMSYS_TYPE, "relation-type", False)] 
        return sum( be.count_tags(pdict, meta=meta)
                    for be, pdict in o._backends_dict.items() )

    def count_lists(self):
        """
        This method is inherited from CoreAllGroup but is unsafe on
        cam.Package. Use instead `count_user_lists`.
        """
        warn("use count_user_lists instead", UnsafeUseWarning, 2)
        return super(_AllGroup, self).count_lists()

    def _count_lists_nowarn(self):
        """
        Allows to call count_lists internally without raising a warning.
        """
        return super(_AllGroup, self).count_lists()


    def count_user_lists(self):
        o = self._owner
        meta = [(CAMSYS_TYPE, None, None)] 
        return sum( be.count_lists(pdict, meta=meta)
                    for be, pdict in o._backends_dict.items() )

    def count_schemas(self):
        o = self._owner
        meta = [(CAMSYS_TYPE, "schema", False)] 
        return sum( be.count_lists(pdict, meta=meta)
                    for be, pdict in o._backends_dict.items() )

class _OwnGroup(CamGroupMixin, CoreOwnGroup):
    def iter_tags(self):
        """
        This method is inherited from CoreOwnGroup but is unsafe on
        cam.Package. Use instead `iter_user_tags`.
        """
        warn("use iter_user_tags instead", UnsafeUseWarning, 2)
        return super(_OwnGroup, self).iter_tags()

    def _iter_tags_nowarn(self):
        """
        Allows to call iter_tags internally without raising a warning.
        """
        return super(_OwnGroup, self).iter_tags()

    def iter_user_tags(self):
        o = self._owner
        for i in o._backend.iter_tags((o._id,),
          meta=[(CAMSYS_TYPE, None, None)]):
            yield o.get_element(i)

    def iter_annotation_types(self):
        o = self._owner
        for i in o._backend.iter_tags((o._id,),
          meta=[(CAMSYS_TYPE, "annotation-type", False)]):
            yield o.get_element(i)

    def iter_relation_types(self):
        o = self._owner
        for i in o._backend.iter_tags((o._id,),
          meta=[(CAMSYS_TYPE, "relation-type", False)]):
            yield o.get_element(i)

    def iter_lists(self, item=None, position=None):
        """
        This method is inherited from CoreOwnGroup but is unsafe on
        cam.Package. Use instead `iter_user_lists`.
        """
        warn("use iter_user_lists instead", UnsafeUseWarning, 2)
        return super(_OwnGroup, self).iter_lists(item=item, position=position)

    def _iter_lists_nowarn(self, item=None, position=None):
        """
        Allows to call iter_lists internally without raising a warning.
        """
        return super(_OwnGroup, self).iter_lists(item=item, position=position)

    def iter_user_lists(self):
        o = self._owner
        for i in o._backend.iter_lists((o._id,),
          meta=[(CAMSYS_TYPE, None, None)]):
            yield o.get_element(i)

    def iter_schemas(self):
        o = self._owner
        for i in o._backend.iter_lists((o._id,),
          meta=[(CAMSYS_TYPE, "schema", False)]):
            yield o.get_element(i)

    def count_tags(self):
        """
        This method is inherited from CoreOwnGroup but is unsafe on
        cam.Package. Use instead `count_user_tags`.
        """
        warn("use count_user_tags instead", UnsafeUseWarning, 2)
        return super(_OwnGroup, self).count_tags()

    def _count_tags_nowarn(self):
        """
        Allows to call count_tags internally without raising a warning.
        """
        return super(_OwnGroup, self).count_tags()

    def count_user_tags(self):
        o = self._owner
        return o._backend.count_tags((o._id,),
            meta=[(CAMSYS_TYPE, None, None)])

    def count_annotation_types(self):
        o = self._owner
        return o._backend.count_tags((o._id,),
            meta=[(CAMSYS_TYPE, "annotation-type", False)])

    def count_relation_types(self):
        o = self._owner
        return o._backend.count_tags((o._id,),
            meta=[(CAMSYS_TYPE, "relation-type", False)])

    def count_lists(self):
        """
        This method is inherited from CoreOwnGroup but is unsafe on
        cam.Package. Use instead `count_user_lists`.
        """
        warn("use count_user_lists instead", UnsafeUseWarning, 2)
        return super(_OwnGroup, self).count_lists()

    def _count_lists_nowarn(self):
        """
        Allows to call count_lists internally without raising a warning.
        """
        return super(_OwnGroup, self).count_lists()

    def count_user_lists(self):
        o = self._owner
        return o._backend.count_lists((o._id,),
            meta=[(CAMSYS_TYPE, None, None)])

    def count_schemas(self):
        o = self._owner
        return o._backend.count_lists((o._id,),
            meta=[(CAMSYS_TYPE, "schema", False)])

class Package(CorePackage):

    # use CAM subclasses as element factories
    annotation_factory = Annotation
    all_factory = _AllGroup
    import_factory = Import
    list_factory = List
    media_factory = Media
    relation_factory = Relation
    resource_factory = Resource
    own_factory = _OwnGroup
    query_factory = Query
    tag_factory = Tag
    view_factory = View

    def __init__(self, url, create=False, readonly=False, force=False):
        CorePackage.__init__(self, url, create, readonly, force)
        if self.url != BOOTSTRAP_URI and self.uri != BOOTSTRAP_URI \
        and self.own.count_imports(uri=BOOTSTRAP_URI) == 0:
            global _bootstrap_ref
            b = _bootstrap_ref()
            if b is None:
                b = Package(BOOTSTRAP_URI, readonly=True)
                _bootstrap_ref = wref(b)
            self.create_import("cam", b)

        ns = self._get_namespaces_as_dict()
        ns.setdefault(DC_NS_PREFIX, "dc")
        self._set_namespaces_with_dict(ns)
        if create:
            bk.init(self, self)
        self.connect("modified-meta", bk.update)
        self.connect("created", bk.init)
        self.connect("tag::added", bk.update)
        self.connect("tag::removed", bk.update)

    def create_tag(self, id):
        """
        This method is inherited from core.Package but is unsafe on
        cam.Package. Use instead `create_user_tag`.

        :see: `create_user_tag`, `create_annotation_type`, 
              `create_relation_type`
        """
        warn("use create_user_tag instead", UnsafeUseWarning, 2)
        return super(Package, self).create_tag(id)

    def create_user_tag(self, id):
        """FIXME: missing docstring.
        """
        return super(Package, self).create_tag(id)

    def create_annotation_type(self, id):
        """FIXME: missing docstring.
        """
        at = super(Package, self).create_tag(id)
        at.enter_no_event_section()
        try:
            at._set_camsys_type("annotation-type")
        finally:
            at.exit_no_event_section()
        return at

    def create_relation_type(self, id):
        """FIXME: missing docstring.
        """
        rt = super(Package, self).create_tag(id)
        rt.enter_no_event_section()
        try:
            rt._set_camsys_type("relation-type")
        finally:
            rt.exit_no_event_section()
        return rt

    def create_annotation(self, id, media, begin, end,
                                mimetype, model=None, url="", type=None):
        """FIXME: missing docstring.
        """
        assert type is None or hasattr(type, "ADVENE_TYPE") \
            or type.find(":") > 0 # strict ID-ref
        a = super(Package, self).create_annotation(id, media, begin, end,
                                                   mimetype, model, url)
        if type:
            type_is_element = hasattr(type, "ADVENE_TYPE")
            a.enter_no_event_section()
            if type_is_element: type.enter_no_event_section()
            try:
                a.type = type
            finally:
                if type_is_element: type.exit_no_event_section()
                a.exit_no_event_section()
        return a

    def create_relation(self, id, mimetype="x-advene/none", model=None,
                        url="", members=(), type=None):
        """FIXME: missing docstring.
        """
        assert type is None or hasattr(type, "ADVENE_TYPE") \
            or type.find(":") > 0 # strict ID-ref
        r = super(Package, self).create_relation(id, mimetype, model, url,
                                                 members)
        if type:
            type_is_element = hasattr(type, "ADVENE_TYPE")
            r.enter_no_event_section()
            if type_is_element: type.enter_no_event_section()
            try:
                r.type = type
            finally:
                if type_is_element: type.exit_no_event_section()
                r.exit_no_event_section()
        return r

    def create_list(self, id, items=()):
        """
        This method is inherited from core.Package but is unsafe on
        cam.Package. Use instead `create_user_list`.

        :see: `create_user_list`, `create_schema`
        """
        warn("use create_user_list instead", UnsafeUseWarning, 2)
        return super(Package, self).create_list(id, items)

    def create_user_list(self, id, items=()):
        """FIXME: missing docstring.
        """
        return super(Package, self).create_list(id, items)

    def create_schema(self, id, items=()):
        """FIXME: missing docstring.
        """
        sc = super(Package, self).create_list(id, items)
        sc.enter_no_event_section()
        try:
            sc._set_camsys_type("schema")
        finally:
            sc.exit_no_event_section()
        return sc

    def associate_tag(self, element, tag):
        """
        This method is inherited from core.Package but is unsafe on
        cam.Package. Use instead `associate_user_tag`.
        """
        warn("use associate_user_tag instead", UnsafeUseWarning, 2)
        super(Package, self).associate_tag(element, tag)

    def _associate_tag_nowarn(self, element, tag):
        """
        Allows to call associate_tag internally without raising a warning.
        """
        super(Package, self).associate_tag(element, tag)


    def dissociate_tag(self, element, tag):
        """
        This method is inherited from core.Package but is unsafe on
        cam.Package. Use instead `dissociate_user_tag`.
        """
        warn("use associate_user_tag instead", UnsafeUseWarning, 2)
        super(Package, self).dissociate_tag(element, tag)

    def _dissociate_tag_nowarn(self, element, tag):
        """
        Allows to call dissociate_tag internally without raising a warning.
        """
        super(Package, self).dissociate_tag(element, tag)

    def associate_user_tag(self, element, tag):
        """
        FIXME: missing docstring.
        """
        if hasattr(tag, "ADVENE_TYPE"):
            systemtype = tag.get_meta(CAMSYS_TYPE, None)
        else:
            # tag is must be a strict id-ref; assume everything is ok
            systemtype = None
        if systemtype is not None:
            raise SemanticError("Tag %s is not simple: %s" %
                                (tag._id, systemtype))
        super(Package, self).associate_tag(element, tag)

    def dissociate_user_tag(self, element, tag):
        """
        FIXME: missing docstring.
        """
        systemtype = tag.get_meta(CAMSYS_TYPE, None)
        if systemtype is not None:
            raise SemanticError("Tag %s is not simple: %s", tag._id, systemtype)
        super(Package, self).dissociate_tag(element, tag)

    # TALES shortcuts

    @property
    def _tales_annotation_types(self):
        return self.all.annotation_types

    @property
    def _tales_relation_types(self):
        return self.all.relation_types

    @property
    def _tales_schemas(self):
        return self.all.schemas

    @property
    def _tales_medias(self):
        return self.all.medias

_bootstrap_ref = lambda: None

Package.make_metadata_property(bk.CREATOR, default="")
Package.make_metadata_property(bk.CONTRIBUTOR, default="")
Package.make_metadata_property(bk.CREATED, default="")
Package.make_metadata_property(bk.MODIFIED, default="")

Package.make_metadata_property(DC_NS_PREFIX + "title", default="")
Package.make_metadata_property(DC_NS_PREFIX + "description", default="")

Package.make_metadata_property(RDFS_NS_PREFIX + "seeAlso", default=None)
