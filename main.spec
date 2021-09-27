# -*- mode: python ; coding: utf-8 -*-
from kivy_deps import sdl2, glew
block_cipher = None

data_spec = [(r'C:/Users/EmpropazTI/Pictures/corpMundialMujer-master/windows/*.kv','./windows'),
            (r'C:/Users/EmpropazTI/Pictures/corpMundialMujer-master/images/*.png','./images'),
            (r'C:/Users/EmpropazTI/Pictures/corpMundialMujer-master/fonts/*.ttf','./fonts'),
            (r'C:/Users/EmpropazTI/Pictures/corpMundialMujer-master/declarations/*.py','./declarations'),
            (r'C:/Users/EmpropazTI/Pictures/corpMundialMujer-master/declarations/*.kv','./declarations'),
            (r'C:/Users/EmpropazTI/Pictures/corpMundialMujer-master/databases/parametric/*.db','./databases/parametric'),
            (r'C:/Users/EmpropazTI/Pictures/corpMundialMujer-master/databases/register/*.db','./databases/register'),
            (r'C:/Users/EmpropazTI/Pictures/corpMundialMujer-master/codes/*.py','./codes')]

a = Analysis(['C:\\Users\\EmpropazTI\\Pictures\\corpMundialMujer-master\\main.py'],
             pathex=['C:\\Users\\EmpropazTI\\Pictures\\corpMundialMujer-master\\windows\\windows apk'],
             binaries=[],
             datas=data_spec,
             hiddenimports=['pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='cmm',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='cmm')


CREATE TABLE [tipo_de_documento] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [ciudades] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL,
  [fkDepartment] int NOT NULL
);
GO
CREATE TABLE [departamentos] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL,
  [fkCountry] int NOT NULL,
  [indicative] int NOT NULL
);
GO
CREATE TABLE [paises] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [rotulos] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [barrios] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL,
  [fkCities] int NOT NULL
);
GO
CREATE TABLE [tipo_de_beneficiario] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [rangos_de_edad] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [entornos] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [sexo] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [genero] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [grupo_etnico] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [discapacidades] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [sector_empresarial] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [ciiu] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [como_surge] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [tiempo_a_dedicar] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [estudios] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [si_no] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [producto_o_servicio] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [porcentaje_de_inversion] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [tiempo_semanal] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [por_que_no] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [regimen_de_salud] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [estado_civil] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [tipos_de_contrato] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [promedio_de_ingresos] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [quien_define_el_ingreso] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [tipo_de_casa] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [material_de_la_casa] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [combustible_de_cocina] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [antiguedad_de_la_casa] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [bancamia] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [de_quien_depende] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [donde_opera] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [alerta_seguimiento] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [caracteristicas_del_hogar] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [categorias_diagnostico_empresarial] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [estado_del_beneficiario] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [estado_meta] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [etapa_del_proceso] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [lineas_de_desarrollo] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [plan_de_inversiones] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [preguntas_de_diagnostico] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [preguntas_diagnostico_empresarial] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [respuestas_diagnostico_empresarial] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [seguimiento_desembolso] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [tipo_de_credito] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [tipo_visita] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO
CREATE TABLE [vulnerabilidad] (
  [id] int NOT NULL,
  [data] varchar(255) NOT NULL
);
GO

SELECT *FROM SYSOBJECTS WHERE  xtype = 'U';
GO