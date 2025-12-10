# 17293746 - Crooked Arrow

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Qufim Island (ID: 126) |
| Block Size       | 140 bytes              |
| Total Events     | 3                      |
| References Count | 15                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [1](#event-1)            | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     39 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x28398     |      164760 |
|       1 | 0xFFFFB317  |  4294947607 |
|       2 | 0xFFFFB2F3  |  4294947571 |
|       3 | 0x080B      |        2059 |
|       4 | 0x000A      |          10 |
|       5 | 0x0028      |          40 |
|       6 | 0x25670     |      153200 |
|       7 | 0xFFFFB53A  |  4294948154 |
|       8 | 0xFFFFB2BF  |  4294947519 |
|       9 | 0x1FA50     |      129616 |
|      10 | 0xFFFFDC44  |  4294958148 |
|      11 | 0xFFFFB1AA  |  4294947242 |
|      12 | 0x12500     |       75008 |
|      13 | 0x651C      |       25884 |
|      14 | 0xFFFFB3A1  |  4294947745 |

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=164.760*, z=-19.689*, y=-19.725*, direction=181.0°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 39 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   1C 04 80 32 05             ...2.
0010: 80 1F 00 06 80 07 80 08  80 1F 01 1F 00 09 80 0A  ................
0020: 80 0B 80 1F 01 1F 00 0C  80 0D 80 0E 80 1F 01 22  ..............."
0030: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x000B [0x1C] WAIT(10* ticks)
  1: 0x000E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0011 [0x1F] MOVE_ENTITY: EventEntity moves to X=153.200*, Z=-19.142*, Y=-19.777*
  3: 0x0019 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=129.616*, Z=-9.148*, Y=-20.054*
  5: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=75.008*, Z=25.884*, Y=-19.551*
  7: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x002F [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  9: 0x0031 [0x00] END_REQSTACK()
```
