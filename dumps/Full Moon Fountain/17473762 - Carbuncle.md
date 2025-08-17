# 17473762 - Carbuncle

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Full Moon Fountain (ID: 170) |
| Block Size       | 148 bytes                    |
| Total Events     | 4                            |
| References Count | 10                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32000](#event-32000)    | 0x0001       |     16 |              3 |
| [32001](#event-32001)    | 0x0011       |     16 |              3 |
| [65535.1](#event-655351) | 0x0021       |     41 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x52B50     |      338768 |
|       1 | 0xFFFAD30A  |  4294628106 |
|       2 | 0xB94D      |       47437 |
|       3 | 0x03F6      |        1014 |
|       4 | 0x533EC     |      340972 |
|       5 | 0xFFFACBC5  |  4294626245 |
|       6 | 0xB9A0      |       47520 |
|       7 | 0x0CE3      |        3299 |
|       8 | 0x0078      |         120 |
|       9 | 0x0198      |         408 |

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

### Event 32000

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 37  00 80 01 80 02 80 03 80   ......7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=338.768*, z=-339.190*, y=47.437*, direction=89.1°*
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 32001

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    92 01 F8 FF FF 7F 37  04 80 05 80 06 80 07 80   ......7........
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0011 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0017 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=340.972*, z=-341.051*, y=47.520*, direction=289.9°*
  2: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 41 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    1C 08 80 5B 09 80 F8  FF FF 7F F8 FF FF 7F 00   ...[...........
0030: FE FE FE 22 00 80 F8 FF  FF 7F 5B 09 80 F8 FF FF  ..."......[.....
0040: 7F F8 FF FF 7F 70 6F 70  30 00                    .....pop0.      
```

#### Opcodes

```
  0: 0x0021 [0x1C] WAIT(120* ticks)
  1: 0x0024 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity], work=408*
  2: 0x0033 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x0035 [0x80] LOAD_WAIT(entity=EventEntity)
  4: 0x003A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pop0" with entities [EventEntity, EventEntity], work=408*
  5: 0x0049 [0x00] END_REQSTACK()
```
