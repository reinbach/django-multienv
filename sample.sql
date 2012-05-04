BEGIN;
CREATE TABLE "order_order" (
    "id" serial NOT NULL PRIMARY KEY,
    "order_number" varchar(20) NOT NULL,
    "amount" numeric(8, 2) NOT NULL
)
;
COMMIT;