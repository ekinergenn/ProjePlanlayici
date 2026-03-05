class Proje:
    def __init__(self,ad:str,amac:str,ilerleme:float,yapilacaklar:list,github:str,diller:list,dosya:str):
        self.ad = ad
        self.amac = amac
        self.ilerleme = ilerleme
        self.yapilacaklar = yapilacaklar
        self.github = github
        self.diller = diller
        self.dosya =dosya

    @classmethod
    def from_dict(cls, veri: dict):
        return cls(
            veri["ad"],
            veri["amac"],
            veri["ilerleme"],
            veri["yapilacaklar"],
            veri["github"],
            veri["diller"],
            veri["dosya"]
        )

    def sozluk_veri(self) -> dict:
        veri = {
            "ad":"",
            "amac":"",
            "ilerleme":0,
            "yapilacaklar":[],
            "github":"",
            "diller":[],
            "dosya":""
        }

        veri["ad"] = self.ad
        veri["amac"] = self.amac
        veri["ilerleme"] = self.ilerleme
        veri["yapilacaklar"] = self.yapilacaklar
        veri["github"] = self.github
        veri["diller"] = self.diller
        veri["dosya"] = self.dosya
        return veri
