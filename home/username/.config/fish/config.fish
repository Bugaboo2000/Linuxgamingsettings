if status is-interactive
    # Commands to run in interactive sessions can go here
end

export VDPAU_DRIVER=nvidia
export __GL_THREADED_OPTIMIZATION=1
export mesa_glthread=true
export GST_VAAPI_ALL_DRIVERS=1
export vblank_mode=0
export __GL_SYNC_TO_VBLANK=0
export LIBVA_DRIVER_NAME=vdpau
export __GL_SHADER_DISK_CACHE_SKIP_CLEANUP=1