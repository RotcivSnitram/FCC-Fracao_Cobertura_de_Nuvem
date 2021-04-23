'''
Documentação:
Gráficos time series dos anos de 2015 e 2016 nas coordenadas do CRIOSFERA 1 (84°S 79.9°W)
'''

# Biblioteca
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LATITUDE_FORMATTER, LONGITUDE_FORMATTER

# Conjunto de dados
data = xr.open_dataset('D:/RotcivSnitram/Documents/CBPF/CRE4AT/ERA5/fcc_2015-2016_monthly_37levels_ant.nc')
print(data)

# Extraindo um subset
#data_subset = data.slice(longitude = slice(-82.5, -77.5), latitude = slice(-81.5, -86.5), level = slice())

# Salvando o novo dataset como um arquivo NetCDF
#data_subset.to_netcdf('arquivo.nc')

# Extraindo as variáveis
cc = data['cc']

# Selecionando dados pelo índice
#cc.isel(longitude = slice(0, 12), latitude = slice(0, 12), level = slice(0, 11))

# Selecionando dados pelos labels
#cc.sel(longitude = slice(-82.5, -77.5), latitude = slice(-81.5, -86.5), level = slice(0, 11))

# Extraindo dados de um ponto de grade
#cc.sel(longitude = -79.9, latitude = -84.0, method = 'nearest').isel(level = 14)

# Configuração do gráficos
#t.sel(longitude = -79.9, latitude = -84.0, method = 'nearest').isel(level = 25).plot()
plt.plot(cc.sel(longitude = -79.9, latitude = -84.0, method = 'nearest').isel(level = 25), 'r-', label = 'FCC')
plt.xlabel("tempo")
plt.ylabel("fcc")
plt.title('Fração de cobertura de nuvens - Criosfera 1')
plt.legend()
plt.grid(True)
plt.show()

#plt.plot(cc.sel(longitude = -79.9, latitude = -84.0, method = 'nearest').isel(time = 1), 'r-', label = 'FCC')
cc.isel(time = 6).sel(longitude = -79.9, latitude = -84.0, method = 'nearest').plot(y = 'level', yincrease = False)
plt.xlabel("fcc")
plt.ylabel("pressão (milibars)")
plt.title('Fração de cobertura de nuvens - Criosfera 1')
plt.legend()
plt.grid(True)
plt.show()

# Configuração do mapa
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection = ccrs.Orthographic(central_longitude=0.0, central_latitude=-90.0, globe=None))

# Criando matrizes de longitude e latitude
lon, lat = np.meshgrid(cc.longitude, cc.latitude)


im = ax.contourf(lon, lat, cc.isel(time = 5, level = 25),
                 levels = np.arange(0, 1, 0.01), cmap = 'jet',
                 transform = ccrs.PlateCarree())

# Barra de intensidade
cbar = plt.colorbar(im, ax = ax, pad = 0.06, fraction = 0.023)
cbar.set_label(label = 'FCC', size = 20)
cbar.ax.tick_params(labelsize = 12)

# Adicionando os limites costeiros
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS)

# Adicionando o título da figura
ax.set_title('Fração de cobertura de nuvem', fontsize = 20)

# Adicionando as linhas de grade
g1 = ax.gridlines(crs = ccrs.PlateCarree(), linestyle = '--', color = 'gray', draw_labels = True)

# Removendo os labels do topo e da direita
g1.ylabels_right = False
g1.xlabels_top = False

# Formatando os labels como latitude e longitude
g1.yformatter = LATITUDE_FORMATTER
g1.xformatter = LONGITUDE_FORMATTER
plt.show()