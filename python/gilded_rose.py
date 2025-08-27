# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items, default_quality_decrease_offset: int = 1):
        """
        Rajout de la variable default_quality_decrease_offset indiquant de combien décroit
        par défaut la qualité d'un objet normal.

        :param items:
        :param default_quality_decrease_offset: de combien d'unité décroit la qualité d'un objet normal
        """
        self.items = items
        self.default_quality_decrease_offset = default_quality_decrease_offset

    def update_quality(self):
        """
        J'ai posé comme postulat que le type de produit est déterminé par le prefix de son nom.
        Cette méthode mets à jour le qualité du produit en fonction de son type et du temps restant pour vendre le produit.
        """
        for item in self.items:

            # #########################################################################################################
            # mise à jour de la valeur qualité
            # #########################################################################################################

            if item.name.startswith("Conjured"):
                # La qualité se dégrade deux fois plus rapidement.
                if item.sell_in <= 0:
                    item.quality = max(0, item.quality - 2 * 2 * self.default_quality_decrease_offset)
                else:
                    item.quality = max(0, item.quality - 2 * self.default_quality_decrease_offset)
            elif item.name.startswith("Aged Brie"):
                # "Aged Brie" augmente sa qualité (quality) plus le temps passe.
                # La qualité d'un produit n'est jamais de plus de 50.
                if item.sell_in <= 0:
                    # Une fois que la date de péremption est passée, la qualité se dégrade deux fois plus rapidement.
                    item.quality = min(50, item.quality + 2 * self.default_quality_decrease_offset)
                else:
                    item.quality = min(50, item.quality + self.default_quality_decrease_offset)
            elif item.name.startswith("Backstage"):
                # "Backstage passes", comme le "Aged Brie", augmente sa qualité (quality) plus le temps passe (sellIn) ;
                # - La qualité augmente de 2 quand il reste 10 jours ou moins
                # - et de 3 quand il reste 5 jours ou moins,
                # - mais la qualité tombe à 0 après le concert.
                if item.sell_in <= 0:
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality =  min(50,item.quality + 3)
                elif item.sell_in <= 10:
                    item.quality =  min(50, item.quality + 2)
                else:
                    item.quality = min(50, item.quality + self.default_quality_decrease_offset)
            elif item.name.startswith("Sulfuras"):
                # "Sulfuras", étant un objet légendaire, n'a pas de date de péremption et ne perd jamais en qualité (quality)
                pass
            else:
                if item.sell_in <= 0:
                    # Une fois que la date de péremption est passée, la qualité se dégrade deux fois plus rapidement.
                    item.quality = max(0, item.quality - 2 *self.default_quality_decrease_offset)
                else:
                    item.quality = max(0, item.quality - self.default_quality_decrease_offset)

            # #########################################################################################################
            # mise à jour de la valeur nombre de jour restant pour vendre l'article
            # #########################################################################################################

            if not item.name.startswith("Sulfuras"):
                item.sell_in = item.sell_in - 1



class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
