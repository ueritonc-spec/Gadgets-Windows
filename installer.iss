#define MyAppName "DesktopGadgets"
#define MyAppVersion "1.3"
#define MyAppPublisher "Carvalho"
#define MyAppExeName "DesktopGadgets.exe"

[Setup]

AppId={{8D0D8D1E-7B34-4A31-A8D7-CHRONOGADGETS}}

AppName={#MyAppName}

AppVersion={#MyAppVersion}

AppPublisher={#MyAppPublisher}

DefaultDirName={autopf}\{#MyAppName}

DefaultGroupName={#MyAppName}

OutputDir=installer

OutputBaseFilename=DesktopGadgetsSetup

Compression=lzma

SolidCompression=yes

WizardStyle=modern

SetupIconFile=icone.ico

UninstallDisplayIcon={app}\{#MyAppExeName}

ArchitecturesInstallIn64BitMode=x64

PrivilegesRequired=admin

CloseApplications=yes

DisableProgramGroupPage=yes

DisableReadyMemo=no

DisableWelcomePage=no

[Languages]

Name: "brazilianportuguese"; \
MessagesFile: "compiler:Languages\BrazilianPortuguese.isl"

[Tasks]

Name: "desktopicon"; \
Description: "Criar atalho na Área de Trabalho"; \
GroupDescription: "Atalhos:"

Name: "startup"; \
Description: "Iniciar DesktopGadgets com Windows"; \
GroupDescription: "Inicialização:"

[Files]

Source: "dist\DesktopGadgets\*"; \
DestDir: "{app}"; \
Flags: recursesubdirs createallsubdirs ignoreversion

[Icons]

Name: "{group}\DesktopGadgets"; \
Filename: "{app}\DesktopGadgets.exe"; \
IconFilename: "{app}\DesktopGadgets.exe"

Name: "{autodesktop}\DesktopGadgets"; \
Filename: "{app}\DesktopGadgets.exe"; \
IconFilename: "{app}\DesktopGadgets.exe"; \
Tasks: desktopicon

[Registry]

Root: HKCU; \
Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; \
ValueType: string; \
ValueName: "DesktopGadgets"; \
ValueData: """{app}\DesktopGadgets.exe"""; \
Tasks: startup; \
Flags: uninsdeletevalue

[Run]

Filename: "{app}\DesktopGadgets.exe"; \
Description: "Abrir DesktopGadgets"; \
Flags: nowait postinstall skipifsilent