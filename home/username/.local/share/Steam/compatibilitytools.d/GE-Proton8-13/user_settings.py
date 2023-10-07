#To enable these settings, name this file "user_settings.py".

#Settings here will take effect for all games run in this Proton version.

user_settings = {
    #By default, logs are saved to $HOME/steam-<STEAM_GAME_ID>.log, overwriting any previous log with that name.
    #Log directory can be overridden with $PROTON_LOG_DIR.

    #Wine debug logging
    "WINEDEBUG": "-all",

    #DXVK debug logging
#    "DXVK_LOG_LEVEL": "info",

    #vkd3d debug logging
#    "VKD3D_DEBUG": "warn",

    #wine-mono debug logging (Wine's .NET replacement)
#    "WINE_MONO_TRACE": "E:System.NotImplementedException",
    #"MONO_LOG_LEVEL": "info",

    #general purpose media logging
#    "GST_DEBUG": "4",
    #or, verbose converter logging (may impact playback performance):
#    "GST_DEBUG": "4,protonaudioconverter:6,protonaudioconverterbin:6,protonvideoconverter:6",

    #Enable DXVK's HUD
    "DXVK_HUD": "compiler, devinfo, fps",

    #Use OpenGL-based wined3d for d3d11, d3d10, and d3d9 instead of Vulkan-based DXVK
#    "PROTON_USE_WINED3D": "1",
#    "LD_PRELOAD": "libgamemodeauto.so",
    "MESA_NO_ERROR": "1",
    "PROTON_FORCE_LARGE_ADDRESS_AWARE": "1",
    "PROTON_ENABLE_NVAPI": "1",
    "DXVK_ENABLE_NVAPI":"1",
    "VDPAU_DRIVER": "nvidia",
    "__GL_THREADED_OPTIMIZATION":"1",
    "mesa_glthread":"true",
    "GST_VAAPI_ALL_DRIVERS":"1",
    "vblank_mode":"0",
    "__GL_SYNC_TO_VBLANK":"0",
    "LIBVA_DRIVER_NAME":"vdpau",
    "WINE_FULLSCREEN_FSR":"1",
    "WINE_FULLSCREEN_FSR_STRENGTH":"performance",
    "__GL_SHADER_DISK_CACHE_SKIP_CLEANUP":"1",

    #Disable d3d11 entirely
#    "PROTON_NO_D3D11": "1",

    #Disable eventfd-based in-process synchronization primitives
    "PROTON_NO_ESYNC": "1"
 

    #Disable futex-based in-process synchronization primitives
#    "PROTON_NO_FSYNC": "1"
}
