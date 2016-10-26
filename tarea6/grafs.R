library(dplyr)
library(ggplot2)

source("utils.R")

datos_cat <- read_psv("out_cat.psv")

datos_part <- read_psv("out_part.psv")

#Grafica catalan
#Tiempo
datos_cat %>% 
  ggplot() +
  geom_point(aes(n, tiempo), alpha = 0.6) +
  theme_bw() +
  scale_colour_continuous(low = "grey", high = "black", na.value = "white")
#Llamadas a funcion
datos_cat %>% 
  ggplot() +
  geom_point(aes(n,llamadas), alpha = 0.6) +
  theme_bw() +
  scale_colour_continuous(low = "grey", high = "black", na.value = "white")


#Grafica de particion
#Tiempo
datos_part %>% 
  ggplot() +
  geom_point(aes(n, m, size = tiempo, color = tiempo), alpha = 0.6) +
  theme_bw() +
  scale_colour_continuous(low = "grey", high = "black", na.value = "white")
#Llamadas a funcion
datos_part %>% 
  ggplot() +
  geom_point(aes(n, m, color = llamadas), alpha = 0.6) +
  theme_bw() +
  scale_colour_continuous(low = "grey", high = "black", na.value = "white")


rbind(
  (data.frame(tiempo = datos_dp$tiempo) %>% 
    mutate(tipo = "PD")),
  (data.frame(tiempo = datos_rec$tiempo) %>% 
     mutate(tipo = "Rec"))
) %>% 
  ggplot() +
  geom_boxplot(aes(x = tipo, y = tiempo)) +
  theme_bw()




