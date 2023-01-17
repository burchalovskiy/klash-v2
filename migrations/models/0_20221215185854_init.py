from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "admin" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "password" VARCHAR(200) NOT NULL,
    "email" VARCHAR(200) NOT NULL  DEFAULT '',
    "last_login" TIMESTAMPTZ NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON COLUMN "admin"."last_login" IS 'Last Login';
CREATE TABLE IF NOT EXISTS "freereport" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "json_result" JSONB NOT NULL,
    "is_completed" BOOL NOT NULL  DEFAULT False,
    "request_type" VARCHAR(12) NOT NULL  DEFAULT 'vin_number',
    "request_info" VARCHAR(20) NOT NULL
);
COMMENT ON COLUMN "freereport"."request_type" IS 'VIN_NUMBER: vin_number\nNUMBER_PLATE: number_plate';
CREATE TABLE IF NOT EXISTS "offer" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "description" TEXT,
    "reports_included" INT NOT NULL,
    "price" DECIMAL(8,2) NOT NULL,
    "discount_value" DECIMAL(4,2) NOT NULL,
    "is_auth_only" BOOL NOT NULL  DEFAULT True,
    "is_active" BOOL NOT NULL  DEFAULT True
);
CREATE TABLE IF NOT EXISTS "user" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "phone_number" VARCHAR(15) NOT NULL UNIQUE,
    "balance" INT NOT NULL  DEFAULT 0
);
CREATE TABLE IF NOT EXISTS "paidreport" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "json_result" JSONB NOT NULL,
    "is_completed" BOOL NOT NULL  DEFAULT False,
    "free_report_id" UUID NOT NULL REFERENCES "freereport" ("id") ON DELETE CASCADE,
    "user_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "payment" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "status" VARCHAR(9) NOT NULL  DEFAULT 'pending',
    "value" DECIMAL(8,2) NOT NULL,
    "offer_id" INT NOT NULL REFERENCES "offer" ("id") ON DELETE CASCADE,
    "user_id" UUID NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);
COMMENT ON COLUMN "payment"."status" IS 'PENDING: pending\nSUCCEEDED: succeeded\nCANCELED: canceled';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
