# 17293742 - Pherimociel

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qufim Island (ID: 126) |
| Block Size       | 132 bytes              |
| Total Events     | 3                      |
| References Count | 14                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     36 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x28551     |      165201 |
|       1 | 0xFFFFB72A  |  4294948650 |
|       2 | 0xFFFFB2A2  |  4294947490 |
|       3 | 0x0727      |        1831 |
|       4 | 0x0028      |          40 |
|       5 | 0x251AA     |      151978 |
|       6 | 0xFFFFBB53  |  4294949715 |
|       7 | 0xFFFFB120  |  4294947104 |
|       8 | 0x22068     |      139368 |
|       9 | 0xFFFFCBC1  |  4294953921 |
|      10 | 0xFFFFAEE2  |  4294946530 |
|      11 | 0x1A9FE     |      109054 |
|      12 | 0x2861      |       10337 |
|      13 | 0xFFFFB1E1  |  4294947297 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=165.201*, z=-18.646*, y=-19.806*, direction=160.9°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 36 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 1F 00             2....
0010: 05 80 06 80 07 80 1F 01  1F 00 08 80 09 80 0A 80  ................
0020: 1F 01 1F 00 0B 80 0C 80  0D 80 1F 01 22 01 00     ............".. 
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=151.978*, Z=-17.581*, Y=-20.192*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=139.368*, Z=-13.375*, Y=-20.766*
  4: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=109.054*, Z=10.337*, Y=-19.999*
  6: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x002C [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  8: 0x002E [0x00] END_REQSTACK()
```
