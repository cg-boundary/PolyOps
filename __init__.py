# ------------------------------------------------------------------------------- #
# ADDON
# ------------------------------------------------------------------------------- #

bl_info = {
    "name": "PolyOps",
    "description": "Blender Workflow Utilities",
    "author": "KenzoCG",
    "version": (1, 0, 0),
    "blender": (4, 3, 2),
    "location": "View3D",
    "category": "3D View"
}

# ------------------------------------------------------------------------------- #
# REGISTER
# ------------------------------------------------------------------------------- #

def register():
    from .registration import register_addon
    register_addon()


def unregister():
    from .registration import unregister_addon
    unregister_addon()
