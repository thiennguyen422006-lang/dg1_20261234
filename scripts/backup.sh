#!/bin/bash
BACKUP_DIR="backup"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
TARGET_FILE="${BACKUP_DIR}/backup_${TIMESTAMP}.tar.gz"

mkdir -p "$BACKUP_DIR"

if tar -czf "$TARGET_FILE" app/data 2>/dev/null; then
    echo "[SUCCESS] Sao luu thanh cong: $TARGET_FILE"
else
    echo "[ERROR] Sao luu that bai!"
    exit 1
fi
