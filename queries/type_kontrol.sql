SELECT 
    type,
    LENGTH(type) as karakter_uzunlugu,
    COUNT(*) as kayit_sayisi,
    HEX(type) as hex_deger
FROM worksheet 
GROUP BY type 
ORDER BY type; 
