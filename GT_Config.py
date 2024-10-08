class FileType:
    '''处理文件描述'''
    LOCAL = "local"
    ONLINE = "online"
    
    NR_MV = "nr_mv"
    MV = "mv"
    CP = "cp"
    RM = "rm"
    UNZIP = "unzip"
    
    ATTR_ENABLED = "enabled"
    ATTR_DESC = "description"
    
    ATTR_FP = "file_path"
    ATTR_FN = "file_name"
    
    ATTR_WP = "work_path"
    ATTR_SP = "save_path"
    ATTR_TYPE = "type"
    ATTR_URL = "url"
    ATTR_REZIP = "retain_zip"
    ATTR_ACTION = "action_type"
    ATTR_SCRIPT = "script"
    ATTR_VERSION_DEMAND = "version_demand"
    ATTR_CONFIG_OPTION = "config_option"
    ATTR_DEFAULT_CONFIG = "default_config"
    ATTR_SERVER_DETAIL = "server_detail"

DEFAULT_CONFIG = [
    #删除的文件
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"discord相关",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_FN:r"CraftPresence.*\.jar",
        FileType.ATTR_ACTION:FileType.RM
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"默认添加的多人服务器",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_FN:r"defaultserverlist.*\.jar",
        FileType.ATTR_ACTION:FileType.RM
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"更真实的黑暗",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_FN:r"HardcoreDarkness-MC.*\.jar",
        FileType.ATTR_ACTION:FileType.RM,
        FileType.ATTR_SERVER_DETAIL:True
    },
    #下载文件
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"平滑字体",
        FileType.ATTR_URL:"https://mediafilez.forgecdn.net/files/2614/474/SmoothFont-1.7.10-1.15.3.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_SCRIPT:[
            {
                FileType.ATTR_ENABLED:True,
                FileType.ATTR_TYPE:FileType.LOCAL,
                FileType.ATTR_DESC:"兼容平滑字体",
                FileType.ATTR_FP:"config\\angelica-modules.cfg",
                FileType.ATTR_VERSION_DEMAND:">2.6.0",
                FileType.ATTR_CONFIG_OPTION:[("general","enableFontRenderer",False)],
                FileType.ATTR_DEFAULT_CONFIG:"""# Configuration file\n\ngeneral {\n    # Enable Debug Logging [default: false]\n    B:enableDebugLogging=false\n\n    # Enable Dynamic Lights [default: false]\n    B:enableDynamicLights=false\n\n    # Batch drawScreen fonts [Experimental] [default: true]\n    B:enableFontRenderer=false\n\n    # Renders the HUD elements once per tick and reuses the pixels to improve performance. [Experimental] [default: true]\n    B:enableHudCaching=true\n\n    # Enable NotFine features [default: true]\n    B:enableNotFineFeatures=true\n\n    # Enable NotFine Options [default: false]\n    B:enableNotFineOptions=false\n\n    # Enable Reese's Sodium Options [default: true]\n    B:enableReesesSodiumOptions=true\n\n    # Enable Sodium rendering [default: true]\n    B:enableSodium=true\n\n    # Enable Sodium fluid rendering [default: false]\n    B:enableSodiumFluidRendering=false\n\n    # Replace some vanilla render paths with more optimized versions. Disable if you encounter mixin conflicts. [default: true]\n    B:enableVBO=true\n\n    # Fix thread-safety in Extra Utilities rendering [default: true]\n    B:fixExtraUtilsSodiumCompat=true\n\n    # Fix RenderBlockFluid reading the block type from the world access multiple times [default: true]\n    B:fixFluidRendererCheckingBlockAgain=true\n\n    # Fix thread-safety in lotrs rendering [default: true]\n    B:fixLotrSodiumCompat=true\n\n    # Hide downloading terrain screen. [From ArchaicFix] [default: true]\n    B:hideDownloadingTerrainScreen=true\n\n    # Inject QuadProvider rendering into some vanilla blocks [default: false]\n    B:injectQPRendering=false\n\n    # Tweak F3 screen to be closer to modern versions. [From ArchaicFix] [default: true]\n    B:modernizeF3Screen=true\n\n    # Optimize Texture Loading. [From Hodgepodge] [default: true]\n    B:optimizeTextureLoading=true\n\n    # Optimize world update light. [From Hodgepodge] [default: true]\n    B:optimizeWorldUpdateLight=true\n\n    # Show block registry name and meta value in F3, similar to 1.8+. [From ArchaicFix] [default: true]\n    B:showBlockDebugInfo=true\n\n    # Show memory usage during game load. [From ArchaicFix] [default: true]\n    B:showSplashMemoryBar=true\n\n    # Speedup Animations. [From Hodgepodge] [default: true]\n    B:speedupAnimations=true\n}\n\n\n"""
            },
            {
                FileType.ATTR_ENABLED:True,
                FileType.ATTR_TYPE:FileType.LOCAL,
                FileType.ATTR_DESC:"兼容平滑字体",
                FileType.ATTR_FP:"config\\fastcraft.ini",
                FileType.ATTR_VERSION_DEMAND:"<2.5.1",
                FileType.ATTR_CONFIG_OPTION:[("transparent tweaks","enableFontRendererTweaks",False)],
                FileType.ATTR_DEFAULT_CONFIG:"""; FastCraft config\n; created 2024-5-24 13:06:29\n;---\n\n; Settings which have some effect on gameplay or visuals.\n\n; Change them for better performance or when experiencing issues.\n[extra tweaks]\n; Disable animated textures, making them static.\n\n; true = faster\n\n; Valid values: true, false. default: false.\ndisableAnimations = false\n; Use asynchronous culling, i.e. check if parts in the world are visible in a thread.\n\n; Some graphics glitches may result from using it, culling data can be delayed up to 1 frame.\n\n; true = faster\n\n; Valid values: true, false. default: false.\nasyncCulling = false\n; Allow entities with custom name tags to be culled.\n\n; This is a workaround to allow using "invisible" entities for billboard text. They normally have\n\n; invalid bounding boxes, which are incompatible with Fastcraft\'s culling checks.\n\n; Valid values: true, false. default: false.\ncullNamedEntities = false\n; Specify whether unicode text should be rendered at an increased size to approximately match the\n\n; non-unicode font size.\n\n; The setting won\'t have any effect if enableFontRendererTweaks is set to false or another reason\n\n; prevents Fastcraft from applying font renderer code edits like a known incompatibility.\n\n; Valid values: true, false. default: false.\nresizeUnicodeText = false\n\n; Settings purely affecting performance, but not gameplay.\n\n; It\'s recommended to leave the settings in this category alone unless you are experiencing issues.\n[transparent tweaks]\n; Specify whether FastCraft should enable its texture buffering tweak (client side).\n\n; This option is a performance vs memory tradeoff, especially with large texture packs. While\n\n; enabled the native memory use is increased by between 20-50 MB for 16x texture packs and 1-2 GB\n\n; for 64x-128x texture packs with many textures. Ideally the extra memory should fit into the\n\n; graphic card\'s dedicated memory. The auto setting will try to estimate whether there\'s enough\n\n; memory and act accordingly.\n\n; The fastest setting depends on your setup.\n\n; Valid values: true, false, auto. default: auto.\nbufferTextureUpdates = auto\n; Adjust the maximum view distance permitted unless specified otherwise in the options menu or\n\n; server.properties.\n\n; This setting doesn\'t have any effect with Optifine installed.\n\n; Valid values: 16 - 256. default: 32.\nmaxViewDistance = 32\n; Specify the minimum interval for reporting server lag in seconds.\n\n; This affects FastCraft\'s replacement for the vanilla "can\'t keep up" messages. Using a larger\n\n; setting or -1 will reduce lag related log/console spam.\n\n; There\'s no impact on behavior or the lag itself, but only the log warnings.\n\n; The value -1 hides all notifications, 0 shows all.\n\n; Valid values: -1 - 2147483647. default: 300.\nlagWarningInterval = 300\n; Specify whether Fastcraft should enable its culling tweaks.\n\n; This option causes parts of the world that aren\'t possibly visible to not be rendered.\n\n; Valid values: true, false. default: true.\nenableCullingTweaks = true\n; Specify if the font renderer may be tweaked by Fastcraft.\n\n; Disabling this setting can resolve compatibility issues with conflicting mods, but performance\n\n; with lots of rendered text may suffer.\n\n; Valid values: true, false. default: true.\nenableFontRendererTweaks = false\n\n; This section allows to adjust incorrect or overly frequent worldrenderer update calls as seen in\n\n; various mods. Normally those calls cause the server to re-send the affected area and the client\n\n; to redraw it, while often only the former is desired.\n\n; The issue is ideally fixed by the mods themselves, this section helps until that\'s done. If you\n\n; are the mod author of a mod listed in here by default, feel free to contact Player for help\n\n; fixing these issues.\n\n; The syntax is: <class>.<method>=<action>, e.g. my.class=syncte.\n\n; Actions (values) currently available are:\n\n; - ignore: Ignore the calls entirely.\n\n; - syncte: Only synchronize the tile entity at the specified position to the client, no redraw.\n\n; Valid values: ignore, syncte.\n[worldrenderer updates]\n\n; Settings for debugging and workarounds\n[debug]\n; Specify whether FastCraft should monitor biome decorator invocations to try tracking issues with\n\n; "Already decorating!!" exceptions down. This is only for investigating worldgen issues.\n\n; Activating this will decrease world generation performance slightly.\n\n; Valid values: true, false. default: false.\nmonitorBiomeDecorators = false\n\n"""
            }
        ]
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"扭曲空间科技",
        FileType.ATTR_URL:"https://github.com/Nxer/Twist-Space-Technology-Mod/releases/download/0.5.9/TwistSpaceTechnology-0.5.9.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_VERSION_DEMAND:">2.6.1",
        FileType.ATTR_SERVER_DETAIL:True
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"GTNH依赖",
        FileType.ATTR_URL:"https://github.com/GTNewHorizons/CodeChickenLib/releases/download/1.1.6//CodeChickenLib-1.1.6.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_VERSION_DEMAND:["2.4.0","2.4.1"]
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"扭曲空间科技",
        FileType.ATTR_URL:"https://github.com/Nxer/Twist-Space-Technology-Mod/releases/download/0.4.30-GTNH2.6.0-final/TwistSpaceTechnology-0.4.30-GTNH2.6.0-final.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_VERSION_DEMAND:"=2.6.0",
        FileType.ATTR_SERVER_DETAIL:True
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"扭曲空间科技",
        FileType.ATTR_URL:"https://github.com/Nxer/Twist-Space-Technology-Mod/releases/download/0.4.30-GTNH2.5.1-final/TwistSpaceTechnology-0.4.30-GTNH2.5.1-final.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_VERSION_DEMAND:"=2.5.1",
        FileType.ATTR_SERVER_DETAIL:True
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"扭曲空间科技",
        FileType.ATTR_URL:"https://github.com/Nxer/Twist-Space-Technology-Mod/releases/download/0.3.7-TheLast2.4.0Fitted/TwistSpaceTechnology-0.3.7-TheLast2.4.0Fitted.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_VERSION_DEMAND:"=2.4.0",
        FileType.ATTR_SERVER_DETAIL:True
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"零点错误修复",
        FileType.ATTR_URL:"https://github.com/wohaopa/ZeroPointServerBugfix/releases/download/0.6.3/ZeroPointBugfix-0.6.3.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_VERSION_DEMAND:"=2.6.1",
        FileType.ATTR_SERVER_DETAIL:True
    },
    {
        FileType.ATTR_ENABLED:False,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"存档备份",
        FileType.ATTR_URL:"https://mediafilez.forgecdn.net/files/2284/754/AromaBackup-1.7.10-0.1.0.0.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_VERSION_DEMAND:"<2.5.1",
        FileType.ATTR_SERVER_DETAIL:True
    },
    {
        FileType.ATTR_ENABLED:False,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"存档备份前置",
        FileType.ATTR_URL:"https://mediafilez.forgecdn.net/files/2257/644/Aroma1997Core-1.7.10-1.0.2.16.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_VERSION_DEMAND:"<2.5.1",
        FileType.ATTR_SERVER_DETAIL:True
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"FPS减速器",
        FileType.ATTR_URL:"https://mediafilez.forgecdn.net/files/2627/303/FpsReducer-mc1.7.10-1.10.3.jar",
        FileType.ATTR_SP:"mods"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"NEI 拼音搜索",
        # FileType.ATTR_URL:"http://github.com/vfyjxf/NotEnoughCharacters/releases/download/1.7.10-1.5.2/NotEnoughCharacters-1.7.10-1.5.2.jar",
        FileType.ATTR_URL:"https://github.com/GTNewHorizons/NotEnoughCharacters/releases/download/1.7.10-1.5.3-GTNH/nechar-1.7.10-1.5.3-GTNH.jar",
        FileType.ATTR_SP:"mods"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"NEI实用工具",
        FileType.ATTR_URL:"https://github.com/RealSilverMoon/NEI-Utilities/releases/download/0.1.9/neiutilities-0.1.9.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_VERSION_DEMAND:"<2.5.1"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"移除所有雾",
        FileType.ATTR_URL:"https://mediafilez.forgecdn.net/files/2574/985/NoFog-1.7.10b1-1.0.jar",
        FileType.ATTR_SP:"mods"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"根据方块NBT信息显示内容",
        FileType.ATTR_URL:"https://mediafilez.forgecdn.net/files/2388/572/OmniOcular-1.7.10-1.0build103.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_SERVER_DETAIL:True,
        FileType.ATTR_SCRIPT:[
            {
                FileType.ATTR_ENABLED:True,
                FileType.ATTR_TYPE:FileType.ONLINE,
                FileType.ATTR_DESC:"OmniOcular配置脚本文件",
                FileType.ATTR_URL:"https://github.com/Amber-siley/GTNH_add_mod_script/releases/download/oo_config/OmniOcular.zip",
                FileType.ATTR_SP:"config\\OmniOcular",
                FileType.ATTR_ACTION:FileType.UNZIP,
                FileType.ATTR_REZIP:False,
            }
        ]
    },
    {
        FileType.ATTR_ENABLED:False,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"万用皮肤补丁14.6a",
        FileType.ATTR_URL:"https://github.com/Amber-siley/GTNH_add_mod_script/releases/download/CSL/CustomSkinLoader_1.7.10-14.6a.jar",
        FileType.ATTR_SP:"mods"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"创世神",
        FileType.ATTR_URL:"https://mediafilez.forgecdn.net/files/2309/699/worldedit-forge-mc1.7.10-6.1.1-dist.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_SERVER_DETAIL:True
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"创世神UI forge版本",
        FileType.ATTR_URL:"https://mediafilez.forgecdn.net/files/2390/420/WorldEditCuiFe-v1.0.7-mf-1.7.10-10.13.4.1566.jar",
        FileType.ATTR_SP:"mods"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"中文输入修复",
        FileType.ATTR_URL:"https://mediafilez.forgecdn.net/files/4408/526/InputFix-1.7.10-v6.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_VERSION_DEMAND:"<2.5.1"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"支持纤细模型",
        FileType.ATTR_URL:"https://mediafilez.forgecdn.net/files/3212/17/SkinPort-1.7.10-v10d.jar",
        FileType.ATTR_SP:"mods"
    },
    {
        FileType.ATTR_ENABLED:False,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"可编程仓室",
        FileType.ATTR_URL:"https://github.com/reobf/Programmable-Hatches-Mod/releases/download/v0.0.18p12-beta/programmablehatches-0.0.18p12.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_SERVER_DETAIL:True,
    },
    {
        FileType.ATTR_ENABLED:False,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"更好的树叶",
        FileType.ATTR_URL:"https://github.com/reobf/Programmable-Hatches-Mod/releases/download/v0.0.18p12-beta/programmablehatches-0.0.18p12.jar",
        FileType.ATTR_SP:"mods"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"额外玩家渲染",
        FileType.ATTR_URL:"https://mediafilez.forgecdn.net/files/4287/440/extraplayerrenderer-1.7.10-1.0.1.jar",
        FileType.ATTR_SP:"mods"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"合成计算器",
        FileType.ATTR_URL:"https://github.com/Discreater/JustEnoughCalculation/releases/download/1.7.10-3.8.6/JustEnoughCalculation-1.7.10-3.8.6.jar",
        FileType.ATTR_SP:"mods"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"合成辅助",
        FileType.ATTR_URL:"https://mediafilez.forgecdn.net/files/2457/94/craftingtweaks-mc1.7.10-1.0.88.jar",
        FileType.ATTR_SP:"mods"
    },
    {
        FileType.ATTR_ENABLED:False,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"服务器实用工具",
        FileType.ATTR_URL:"https://github.com/GTNewHorizons/ServerUtilities/releases/download/2.0.68-pre/ServerUtilities-2.0.68-pre.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_VERSION_DEMAND:"=2.5.1",
        FileType.ATTR_SERVER_DETAIL:True
    },
    {
        FileType.ATTR_ENABLED:False,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_SERVER_DETAIL:True,
        FileType.ATTR_DESC:"TC4研究助手",
        FileType.ATTR_URL:"https://github.com/wohaopa/TC4Helper/releases/download/V2.2/tc4helper-V2.2.jar",
        FileType.ATTR_SP:"mods"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"连锁挖矿",
        FileType.ATTR_URL:"https://mediafilez.forgecdn.net/files/2435/506/VeinMiner-1.7.10-0.36.0.496%2B28a7f13.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_SERVER_DETAIL:True
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"Replay mod",
        FileType.ATTR_URL:"https://github.com/Amber-siley/GTNH_add_mod_script/releases/download/Replay/replaymod-1.7.10-2.5.2.jar",
        FileType.ATTR_SP:"mods",
        FileType.ATTR_SCRIPT:[
            {
                FileType.ATTR_ENABLED:True,
                FileType.ATTR_TYPE:FileType.ONLINE,
                FileType.ATTR_DESC:"兼容GTNH的Replay修复mod",
                FileType.ATTR_URL:"https://github.com/wohaopa/ReplayModFixMod/releases/download/1.1.0/replaymodfixmod-1.0.0-2-gd836d8f.jar",
                FileType.ATTR_SP:"mods"
            },
            {
                FileType.ATTR_ENABLED:True,
                FileType.ATTR_TYPE:FileType.LOCAL,
                FileType.ATTR_DESC:"Custom Main Menu 配置文件",
                FileType.ATTR_FP:"config\\CustomMainMenu\\mainmenu.json",
                FileType.ATTR_CONFIG_OPTION:[
                    ("buttons","replayviewer",{
                            "text" : "replaymod.gui.replayviewer",
                            "normalTextColor": 4227327,
                            "hoverTextColor": 16758315,
                            "texture" : "mainmenu:textures/btn4.png",
                            "posX" : 0,
                            "posY" : -120,
                            "width" : 150,
                            "height" : 20,
                            "imageWidth" : 1000,
                            "imageHeight" : 1,
                            "alignment": "column_bottom",
                            "wrappedButton": 17890234
                        }
                    ),
                    (("buttons","singleplayer"),"posY",-160),
                    (("buttons","multiplayer"),"posY",-140)
                ]
            },
            {
                FileType.ATTR_ENABLED:True,
                FileType.ATTR_TYPE:FileType.LOCAL,
                FileType.ATTR_DESC:"Custom Main Menu 配置文件",
                FileType.ATTR_FP:"config\\CustomMainMenu\\mainmenu_auto.json",
                FileType.ATTR_CONFIG_OPTION:[
                    ("buttons","replayviewer",{
                            "text" : "replaymod.gui.replayviewer",
                            "normalTextColor": 4227327,
                            "hoverTextColor": 16758315,
                            "texture" : "mainmenu:textures/btn4.png",
                            "posX" : 0,
                            "posY" : -120,
                            "width" : 150,
                            "height" : 20,
                            "imageWidth" : 1000,
                            "imageHeight" : 1,
                            "alignment": "column_bottom",
                            "wrappedButton": 17890234
                        }
                    ),
                    (("buttons","singleplayer"),"posY",-160),
                    (("buttons","multiplayer"),"posY",-140)
                ]
            },
            {
                FileType.ATTR_ENABLED:True,
                FileType.ATTR_TYPE:FileType.LOCAL,
                FileType.ATTR_DESC:"Custom Main Menu 配置文件",
                FileType.ATTR_FP:"config\\CustomMainMenu\\mainmenu_large.json",
                FileType.ATTR_CONFIG_OPTION:[
                    ("buttons","replayviewer",{
                            "text" : "replaymod.gui.replayviewer",
                            "normalTextColor": 4227327,
                            "hoverTextColor": 16758315,
                            "texture" : "mainmenu:textures/btn4.png",
                            "posX" : 0,
                            "posY" : -120,
                            "width" : 150,
                            "height" : 20,
                            "imageWidth" : 1000,
                            "imageHeight" : 1,
                            "alignment": "column_bottom",
                            "wrappedButton": 17890234
                        }
                    ),
                    (("buttons","singleplayer"),"posY",-160),
                    (("buttons","multiplayer"),"posY",-140)
                ]
            },
            {
                FileType.ATTR_ENABLED:True,
                FileType.ATTR_TYPE:FileType.LOCAL,
                FileType.ATTR_DESC:"Custom Main Menu 配置文件",
                FileType.ATTR_FP:"config\\CustomMainMenu\\mainmenu_normal.json",
                FileType.ATTR_CONFIG_OPTION:[
                    ("buttons","replayviewer",{
                            "text" : "replaymod.gui.replayviewer",
                            "normalTextColor": 4227327,
                            "hoverTextColor": 16758315,
                            "texture" : "mainmenu:textures/btn4.png",
                            "posX" : 0,
                            "posY" : -120,
                            "width" : 150,
                            "height" : 20,
                            "imageWidth" : 1000,
                            "imageHeight" : 1,
                            "alignment": "column_bottom",
                            "wrappedButton": 17890234
                        }
                    ),
                    (("buttons","singleplayer"),"posY",-160),
                    (("buttons","multiplayer"),"posY",-140)
                ]
            },
            {
                FileType.ATTR_ENABLED:True,
                FileType.ATTR_TYPE:FileType.LOCAL,
                FileType.ATTR_DESC:"Custom Main Menu 配置文件",
                FileType.ATTR_FP:"config\\CustomMainMenu\\mainmenu_small.json",
                FileType.ATTR_CONFIG_OPTION:[
                    ("buttons","replayviewer",{
                            "text" : "replaymod.gui.replayviewer",
                            "normalTextColor": 4227327,
                            "hoverTextColor": 16758315,
                            "texture" : "mainmenu:textures/btn4.png",
                            "posX" : 0,
                            "posY" : -120,
                            "width" : 300,
                            "height" : 20,
                            "imageWidth" : 1000,
                            "imageHeight" : 1,
                            "alignment": "column_bottom",
                            "wrappedButton": 17890234
                        }
                    ),
                    (("buttons","singleplayer"),"posY",-160),
                    (("buttons","multiplayer"),"posY",-140)
                ]
            }
        ]
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"GTNH-Faithful 材质包",
        FileType.ATTR_URL:"http://github.com/Ethryan/GTNH-Faithful-Textures/releases/download/0.9.6/GTNH-Faithful-Textures.0.9.6.zip",
        FileType.ATTR_SP:"resourcepacks"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"汉化文件",
        FileType.ATTR_URL:"https://github.com/Kiwi233/Translation-of-GTNH/releases/download/2.5.1/2.5.1.7z",
        FileType.ATTR_SP:".",
        FileType.ATTR_ACTION:FileType.UNZIP,
        FileType.ATTR_REZIP:False,
        FileType.ATTR_VERSION_DEMAND:"=2.5.1"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"汉化文件",
        FileType.ATTR_URL:"https://github.com/Kiwi233/Translation-of-GTNH/releases/download/2.5.0/2.5.0.7z",
        FileType.ATTR_SP:".",
        FileType.ATTR_ACTION:FileType.UNZIP,
        FileType.ATTR_REZIP:False,
        FileType.ATTR_VERSION_DEMAND:"=2.5.0"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"汉化文件",
        FileType.ATTR_URL:"https://github.com/Kiwi233/Translation-of-GTNH/releases/download/2.4.1.V2/2.4.1.V2.7z",
        FileType.ATTR_SP:".",
        FileType.ATTR_ACTION:FileType.UNZIP,
        FileType.ATTR_REZIP:False,
        FileType.ATTR_VERSION_DEMAND:"=2.4.1"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"汉化文件",
        FileType.ATTR_URL:"https://github.com/Kiwi233/Translation-of-GTNH/releases/download/2.4.0/2.4.0.7z",
        FileType.ATTR_SP:".",
        FileType.ATTR_ACTION:FileType.UNZIP,
        FileType.ATTR_REZIP:False,
        FileType.ATTR_VERSION_DEMAND:"=2.4.0"
    },
    #移动文件
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"游戏按键设置文件",
        FileType.ATTR_FP:"options.txt",
        FileType.ATTR_SP:".",
        FileType.ATTR_ACTION:FileType.CP
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"旅行地图数据",
        FileType.ATTR_FP:"journeymap",
        FileType.ATTR_SP:"journeymap",
        FileType.ATTR_ACTION:FileType.CP
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"旅行地图矿脉，地下流体",
        FileType.ATTR_FP:"visualprospecting",
        FileType.ATTR_SP:"visualprospecting",
        FileType.ATTR_ACTION:FileType.CP
    },
    {
        FileType.ATTR_ENABLED:False,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"存档文件",
        FileType.ATTR_FP:"saves",
        FileType.ATTR_SP:"saves",
        FileType.ATTR_ACTION:FileType.CP
    },
    {
        FileType.ATTR_ENABLED:False,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"存档备份",
        FileType.ATTR_FP:"backups",
        FileType.ATTR_SP:"backups",
        FileType.ATTR_ACTION:FileType.CP
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"神秘时代灵气节点数据",
        FileType.ATTR_FP:"TCNodeTracker",
        FileType.ATTR_SP:"TCNodeTracker",
        FileType.ATTR_ACTION:FileType.CP
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"optifine视频设置文件",
        FileType.ATTR_FP:"optionsof.txt",
        FileType.ATTR_SP:".",
        FileType.ATTR_ACTION:FileType.CP
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"Angelica视频设置文件",
        FileType.ATTR_FP:"optionsnf.txt",
        FileType.ATTR_SP:".",
        FileType.ATTR_ACTION:FileType.CP
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"aromabackup备份配置",
        FileType.ATTR_FP:"config\\aroma1997\\AromaBackup.cfg",
        FileType.ATTR_SERVER_DETAIL:True,
        FileType.ATTR_CONFIG_OPTION:[("general","delay",360),\
                                    ("general","keep",7),\
                                    ("general","onStartup","false"),\
                                    ("general","compressionRate",9)],
        FileType.ATTR_DEFAULT_CONFIG:"""# Configuration file\n\ngeneral {\n    # If all players or only admins can use the /backup command.\n    B:allPlayers=true\n\n    # If the blacklist is enabled, the dimensions (ids) specified here will not be backed up.\n    I:blacklist <\n     >\n\n    # Compression rate. Has to be between 9 (high compression) and 1 (low compression).\n    I:compressionRate=9\n\n    # How frequently a automatic backup is done in minutes. 0 means Auto-Backup disabled.\n    I:delay=360\n\n    # How many backups are kept. 0 means infinite\n    I:keep=5\n\n    # Where to store the Backups. Either an absolute path or relative to the minecraft folder.\n    S:location=./backups\n\n    # If a backup should be done when the world gets loaded.\n    B:onStartup=true\n\n    # If the scheduled backup should be skipped if no players were on the server since the last one.\n    B:skipbackup=true\n\n    # If this is set to true, it will use the Dimension Whitelist, if it is false, it will use the Dimension Blacklist\n    B:useWhitelist=false\n\n    # If the whitelist is enabled, only the dimensions (ids) specified here will be backed up.\n    I:whitelist <\n        0\n        1\n        -1\n     >\n}\n\n\n"""
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"服务器配置",
        FileType.ATTR_SERVER_DETAIL:True,
        FileType.ATTR_VERSION_DEMAND:">2.6.0",
        FileType.ATTR_FP:"serverutilities\\serverutilities.cfg",
        FileType.ATTR_CONFIG_OPTION:[("world","chunk_claiming",True),
                                        ("world","chunk_loading",True),
                                        ("commands","home",True),
                                        ("commands","backup",True),
                                        ("ranks","enabled",True),
                                        ("backups","enable_backups",True),
                                        ("backups","backup_timer",1),
                                        ("backups","backups_to_keep",7),
                                        ("backups","compression_level",9)],
        FileType.ATTR_DEFAULT_CONFIG:"""# Configuration file\n\nafk {\n    # Enables afk timer.\n    B:enabled=false\n\n    # Enables afk timer in singleplayer.\n    B:enabled_singleplayer=false\n\n    # Will print in console when someone goes/comes back from AFK.\n    B:log_afk=false\n\n    # After how much time it will display notification to all players.\n    S:notificationTimer=5m\n}\n\n\nauto_shutdown {\n    # Enables auto-shutdown.\n    B:enabled=false\n\n    # Enables auto-shutdown in singleplayer worlds.\n    B:enabled_singleplayer=false\n\n    # Server will automatically shut down after X hours.\n    # Time Format: HH:MM. If the system time matches a value, server will shut down.\n    # It will look for closest value available that is not equal to current time.\n    S:times <\n        04:00\n        16:00\n     >\n}\n\n\nbackups {\n    # Path to backups folder.\n    S:backup_folder_path=./backups/\n\n    # Time between backups in hours. \n    # 1.0 - backups every hour 6.0 - backups every 6 hours 0.5 - backups every 30 minutes.\n    S:backup_timer=1\n\n    # Number of backup files to keep before deleting old ones.\n    I:backups_to_keep=7\n\n    # How much the backup file will be compressed. 1 - best speed 9 - smallest file size.\n    I:compression_level=9\n\n    # Prints (current size | total size) when backup is done\n    B:display_file_size=true\n\n    # Enables backups.\n    B:enable_backups=true\n\n    # Backups won\'t run if no players are online.\n    B:need_online_players=true\n\n    # Silence backup notifications.\n    B:silent_backup=false\n\n    # Run backup in a separated thread (recommended)\n    B:use_separate_thread=true\n}\n\n\nchat {\n    # Adds ~ to player names that have changed nickname to prevent trolling.\n    B:add_nickname_tilde=false\n}\n\n\ncommands {\n    B:back=false\n    B:backup=true\n    B:chunks=false\n    B:dump_chunkloaders=false\n    B:dump_permissions=true\n    B:fly=false\n    B:god=false\n    B:heal=false\n    B:home=true\n    B:inv=false\n    B:kickme=false\n    B:killall=false\n    B:leaderboard=false\n    B:mute=false\n    B:nbtedit=false\n    B:nick=false\n    B:ranks=false\n    B:rec=false\n    B:rtp=false\n    B:spawn=false\n    B:tpa=false\n    B:tpl=false\n    B:trash_can=true\n    B:warp=false\n}\n\n\n##########################################################################################################\n# debugging\n#--------------------------------------------------------------------------------------------------------#\n# Don\'t set any values to true, unless you are debugging the mod.\n##########################################################################################################\n\ndebugging {\n    # See dev-only sidebar buttons. They probably don\'t do anything.\n    B:dev_sidebar_buttons=false\n\n    # See GUI widget bounds when you hold B.\n    B:gui_widget_bounds=false\n\n    # Print a message in console every time a chunk is forced or unforced. Recommended to be off, because spam.\n    B:log_chunkloading=false\n\n    # Log config editing.\n    B:log_config_editing=false\n\n    # Log all events that extend EventBase.\n    B:log_events=false\n\n    # Log incoming and outgoing network messages.\n    B:log_network=false\n\n    # Log player teleporting.\n    B:log_teleport=false\n\n    # Print more errors.\n    B:print_more_errors=false\n\n    # Print more info.\n    B:print_more_info=false\n\n    # Enables special debug commands.\n    B:special_commands=false\n}\n\n\ngeneral {\n    # Merges player profiles, in case player logged in without internet connection/in offline mode server. If set to DEFAULT, it will only merge on singleplayer worlds.\n    S:merge_offline_mode_players=true\n\n    # This will replace /reload with ServerUtilities version of it.\n    B:replace_reload_command=true\n}\n\n\nlogin {\n    # Enables message of the day.\n    B:enable_motd=false\n\n    # Enables starting items.\n    B:enable_starting_items=false\n\n    # Message of the day. This will be displayed when player joins the server.\n    S:motd <\n        "Hello player!"\n     >\n\n    # Items to give player when they first join the server.\n    # Format: \'{id:"ID",Count:X,Damage:X,tag:{}}\', Use /print_item to get NBT of item in your hand.\n    S:starting_items <\n     >\n}\n\n\nranks {\n    # Enables ranks and adds command.x permissions and allows ranks to control them.\n    B:enabled=true\n\n    # Adds chat colors/rank-specific syntax.\n    B:override_chat=true\n\n    # Allow to configure commands with ranks. Disable this if you want to use other permission mod for that.\n    B:override_commands=true\n}\n\n\nteam {\n    # Automatically creates a team for player on multiplayer, based on their username and with a random color.\n    B:autocreate_mp=false\n\n    # Automatically creates (or joins) a team on singleplayer/LAN with ID \'singleplayer\'.\n    B:autocreate_sp=true\n    B:disable_teams=false\n\n    # Don\'t allow other players to break blocks in claimed chunks\n    B:grief_protection=true\n\n    # Disable no team notification entirely.\n    B:hide_team_notification=false\n\n    # Don\'t allow other players to interact with blocks in claimed chunks\n    B:interaction_protection=true\n}\n\n\nworld {\n    # Dimensions where chunk claiming isn\'t allowed.\n    I:blocked_claiming_dimensions <\n     >\n\n    # Enables chunk claiming.\n    B:chunk_claiming=true\n\n    # Enables chunk loading. If chunk_claiming is set to false, changing this won\'t do anything.\n    B:chunk_loading=true\n\n    # Disables player damage when they are stuck in walls.\n    B:disable_player_suffocation_damage=false\n\n    # List of items that will have right-click function disabled on both sides.\n    # You can use \'/inv disable_right_click\' command to do with from in-game.\n    # Syntax: modid:item:metadata. Set metadata to * to ignore it.\n    S:disabled_right_click_items <\n     >\n\n    # Allowed values:\n    # DEFAULT = Teams can decide their explosion setting\n    # TRUE = Explosions on for everyone.\n    # FALSE = Explosions disabled for everyone.\n    S:enable_explosions=true\n\n    # Allowed values:\n    # DEFAULT = Players can choose their own PVP status.\n    # TRUE = PVP on for everyone.\n    # FALSE = PVP disabled for everyone.\n    S:enable_pvp=true\n\n    # Locked time in ticks in spawn dimension.\n    # -1 - Disabled\n    # 0 - Morning\n    # 6000 - Noon\n    # 12000 - Evening\n    # 18000 - Midnight\n    I:forced_spawn_dimension_time=-1\n\n    # Locked weather type in spawn dimension.\n    # -1 - Disabled\n    # 0 - Clear\n    # 1 - Raining\n    # 2 - Thunderstorm\n    I:forced_spawn_dimension_weather=-1\n\n    # Max /rtp distance\n    D:rtp_max_distance=100000.0\n\n    # Max tries /rtp does before failure.\n    I:rtp_max_tries=200\n\n    # Min /rtp distance\n    D:rtp_min_distance=1000.0\n\n    # If set to true, explosions and hostile mobs in spawn area will be disabled, players won\'t be able to attack each other in spawn area.\n    B:safe_spawn=false\n\n    # Show play time in corner.\n    B:show_playtime=false\n\n    # Enable spawn area in singleplayer.\n    B:spawn_area_in_sp=false\n\n    # Spawn dimension. Overworld by default.\n    I:spawn_dimension=0\n\n    # Spawn radius. You must set spawn-protection in server.properties file to 0!\n    I:spawn_radius=0\n\n    # Unloads erroring chunks if dimension isn\'t loaded or some other problem occurs.\n    B:unload_erroring_chunks=false\n\n    ##########################################################################################################\n    # logging\n    #--------------------------------------------------------------------------------------------------------#\n    # Logs different events in logs/world.log file.\n    ##########################################################################################################\n\n    logging {\n        # Logs block breaking.\n        B:block_broken=false\n\n        # Logs block placement.\n        B:block_placed=false\n\n        # Enables chat logging.\n        B:chat_enable=false\n\n        # Enables world logging.\n        B:enabled=false\n\n        # Logs player attacks on other players/entites.\n        B:entity_attacked=false\n\n        # Exclude mobs from entity attack logging.\n        B:exclude_mob_entity=false\n\n        # Includes creative players in world logging.\n        B:include_creative_players=false\n\n        # Includes fake players in world logging.\n        B:include_fake_players=false\n\n        # Logs item clicking in air.\n        B:item_clicked_in_air=false\n    }\n\n}\n\n\n"""
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.LOCAL,
        FileType.ATTR_DESC:"服务器配置",
        FileType.ATTR_FP:"serverutilities\\server\\ranks.txt",
        FileType.ATTR_VERSION_DEMAND:">2.6.0",
        FileType.ATTR_SERVER_DETAIL:True,
        FileType.ATTR_CONFIG_OPTION:[("player","serverutilities.claims.max_chunks",300),
                                        ("player","serverutilities.chunkloader.max_chunks",300),
                                        ("player","serverutilities.homes.max",100),
                                        ("player","serverutilities.homes.cross_dim",True),
                                        ("vip","serverutilities.homes.cross_dim",True),
                                        ("admin","serverutilities.homes.cross_dim",True),
                                        ("vip","serverutilities.homes.max",100),
                                        ("admin","serverutilities.homes.max",100),
                                        ("admin","serverutilities.homes.max",100),
                                        ("vip","serverutilities.chunkloader.max_chunks",500)],
        FileType.ATTR_DEFAULT_CONFIG:"""// For more info visit https://github.com/GTNewHorizons/ServerUtilities\n\n[player]\ndefault_player_rank: true\npower: 1\nserverutilities.claims.max_chunks: 300\nserverutilities.chunkloader.max_chunks: 300\nserverutilities.homes.max: 100\nserverutilities.homes.warmup: 5s\nserverutilities.homes.cooldown: 5s\nserverutilities.homes.cross_dim: true\n\n[vip]\npower: 20\nserverutilities.chat.name_format: <&bVIP {name}&r>\nserverutilities.claims.max_chunks: 500\nserverutilities.chunkloader.max_chunks: 500\nserverutilities.homes.max: 100\nserverutilities.homes.warmup: 0s\nserverutilities.homes.cooldown: 1s\nserverutilities.homes.cross_dim: true\n\n[admin]\ndefault_op_rank: true\npower: 100\nserverutilities.chat.name_format: <&2{name}&r>\nserverutilities.claims.max_chunks: 1000\nserverutilities.chunkloader.max_chunks: 1000\nserverutilities.claims.bypass_limits: true\nserverutilities.homes.max: 100\nserverutilities.homes.warmup: 0s\nserverutilities.homes.cooldown: 0s\nserverutilities.homes.cross_dim: true"""
    }
]

DEFAULT_CHINESE_CONFIG = [
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"汉化文件",
        FileType.ATTR_URL:"https://github.com/Kiwi233/Translation-of-GTNH/releases/download/2.5.1/2.5.1.7z",
        FileType.ATTR_SP:".",
        FileType.ATTR_ACTION:FileType.UNZIP,
        FileType.ATTR_REZIP:False,
        FileType.ATTR_VERSION_DEMAND:"=2.5.1"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"汉化文件",
        FileType.ATTR_URL:"https://github.com/Kiwi233/Translation-of-GTNH/releases/download/2.5.0/2.5.0.7z",
        FileType.ATTR_SP:".",
        FileType.ATTR_ACTION:FileType.UNZIP,
        FileType.ATTR_REZIP:False,
        FileType.ATTR_VERSION_DEMAND:"=2.5.0"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"汉化文件",
        FileType.ATTR_URL:"https://github.com/Kiwi233/Translation-of-GTNH/releases/download/2.4.1.V2/2.4.1.V2.7z",
        FileType.ATTR_SP:".",
        FileType.ATTR_ACTION:FileType.UNZIP,
        FileType.ATTR_REZIP:False,
        FileType.ATTR_VERSION_DEMAND:"=2.4.1"
    },
    {
        FileType.ATTR_ENABLED:True,
        FileType.ATTR_TYPE:FileType.ONLINE,
        FileType.ATTR_DESC:"汉化文件",
        FileType.ATTR_URL:"https://github.com/Kiwi233/Translation-of-GTNH/releases/download/2.4.0/2.4.0.7z",
        FileType.ATTR_SP:".",
        FileType.ATTR_ACTION:FileType.UNZIP,
        FileType.ATTR_REZIP:False,
        FileType.ATTR_VERSION_DEMAND:"=2.4.0"
    },
]