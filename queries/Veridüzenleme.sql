##VERİ DÜZENLEME 


UPDATE WORKSHEET
SET type = 'İTHAL'
WHERE type LIKE 'İTHAL..';



UPDATE worksheet
SET max_price = ROUND(max_price, 2),
    avg_price = ROUND(avg_price, 2),
    min_price = ROUND(min_price, 2)
WHERE max_price IS NOT NULL AND avg_price IS NOT NULL AND min_price IS NOT NULL;



DELETE FROM worksheet
WHERE LOWER(name) LIKE '%ithal%' OR LOWER(name) LIKE '%yerli%';