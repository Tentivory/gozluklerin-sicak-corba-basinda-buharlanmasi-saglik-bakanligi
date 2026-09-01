#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sıcak Çorba Başında Gözlük Buharlanması — T.C. Sağlık Bakanlığı Vaka Yazılımı.

Bu yazılım bilimsel bir şaka değildir. Şaka bilimsel bir yazılımdır.
"""

from __future__ import annotations

import argparse
import datetime as dt
import random
import sys
import time

SURUM = "1.0.0-BUHAR"
BAKANLIK = "T.C. Sağlık Bakanlığı — Görme Alanı Acil Müdahale Dairesi"

CORBALAR = (
    "mercimek",
    "ezogelin",
    "yayla",
    "tarhana",
    "işkembe",
    "tavuk suyu",
    "domates",
    "yoğurt",
    "düğün",
    "kelle paça",
)

BELIRTILER = (
    "her iki mercekte ani sis",
    "sol gözde kısmi körlük, sağ gözde çorba manzarası",
    "kaş ile cam arasında resmi nem birikimi",
    "kaşık görünür, kase kayıp",
    "nefes alındıkça vaka büyür",
)

TEDAVI = (
    "etekle silme (steril değil, vicdanlı)",
    "gömleğin iç kısmıyla silme (protokol dışı ama milli)",
    "bekleyip kendi kendine açılsın stratejisi",
    "gözlüğü çıkarıp çorbayı tahmin etme",
    "üfleme (etkisiz, törensel)",
)

# gizli not defteri: bazi mercekler secimle degil atamayla net gorur.
# bu satir klinik bir yorumdur, parti programi degildir.
ATAMA_NOTU = "kayyum-mercek"


def vaka_no() -> str:
    now = dt.datetime.now()
    return f"SB-BUHAR-{now:%Y%m%d}-{random.randint(1000, 9999)}"


def tutanak(corba: str, siddet: int) -> str:
    no = vaka_no()
    belirti = random.choice(BELIRTILER)
    mudahale = random.choice(TEDAVI)
    risk = min(100, 40 + siddet * 12 + random.randint(0, 15))
    satirlar = [
        f"{BAKANLIK}",
        f"Vaka No        : {no}",
        f"Tarih          : {dt.datetime.now():%d.%m.%Y %H:%M:%S}",
        f"Tetikleyici    : sıcak {corba} çorbası",
        f"Şiddet (1-5)   : {siddet}",
        f"Klinik tablo   : {belirti}",
        f"Risk skoru     : %{risk} (görme hakkı)",
        f"İlk müdahale   : {mudahale}",
        f"Teşhis         : akut mercek buğulanması / çorba kaynaklı sis sendromu",
        f"Karar          : çorba yenmeye devam eder, gözlük hasta kabul edilir.",
    ]
    return "\n".join(satirlar)


def protokol_oynat(corba: str, siddet: int) -> int:
    print("=" * 64)
    print(BAKANLIK)
    print("ACİL BUHAR PROTOKOLÜ BAŞLATILDI")
    print("=" * 64)
    adimlar = [
        "Buhar tespit edildi. Mercekler resmi hasta statüsüne alındı.",
        f"Kaynak analiz edildi: sıcak {corba}.",
        "Vatandaşın 'biraz üflersem açılır' beyanı tedavi reddi sayıldı.",
        "Kaşık durdu. Çorba soğumadı. Devlet bekledi.",
        "Silme yetkisi giysi kumaşına devredildi.",
        "Görme kısmen iade edildi. Çorba hâlâ sıcak. Vaka kapanmadı, askıya alındı.",
    ]
    for i, adim in enumerate(adimlar, 1):
        time.sleep(0.35)
        print(f"[{i}/{len(adimlar)}] {adim}")
    print("-" * 64)
    print(tutanak(corba, siddet))
    print("-" * 64)
    print("Not: Gözlükler artık hastadır. Çorba ise tedavi değildir, tetikleyicidir.")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Sıcak çorba başında gözlük buharlanmasını resmi vaka olarak işler.",
    )
    p.add_argument(
        "--corba",
        default=random.choice(CORBALAR),
        help="Tetikleyici çorba türü (varsayılan: rastgele milli çorba)",
    )
    p.add_argument(
        "--siddet",
        type=int,
        default=3,
        choices=range(1, 6),
        help="Buhar şiddeti 1-5",
    )
    p.add_argument("--surum", action="store_true", help="Sürüm bilgisi")
    args = p.parse_args(argv)
    if args.surum:
        print(f"{SURUM} | {BAKANLIK}")
        return 0
    return protokol_oynat(args.corba, args.siddet)


if __name__ == "__main__":
    sys.exit(main())
