# 17473764 - Carbuncle

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Full Moon Fountain (ID: 170) |
| Block Size       | 180 bytes                    |
| Total Events     | 5                            |
| References Count | 14                           |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32000](#event-32000)    | 0x0001       |     16 |              3 |
| [32001](#event-32001)    | 0x0011       |     16 |              3 |
| [65535.1](#event-655351) | 0x0021       |     41 |              6 |
| [65535.2](#event-655352) | 0x004A       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x5265B     |      337499 |
|       1 | 0xFFFAD451  |  4294628433 |
|       2 | 0xB9B6      |       47542 |
|       3 | 0x02BD      |         701 |
|       4 | 0x521E4     |      336356 |
|       5 | 0xFFFAC595  |  4294624661 |
|       6 | 0xBB50      |       47952 |
|       7 | 0x0594      |        1428 |
|       8 | 0x00B4      |         180 |
|       9 | 0x0198      |         408 |
|      10 | 0x0024      |          36 |
|      11 | 0x52BC5     |      338885 |
|      12 | 0xFFFAC9A4  |  4294625700 |
|      13 | 0xB9A3      |       47523 |

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
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=337.499*, z=-338.863*, y=47.542*, direction=61.6°*
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
  1: 0x0017 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=336.356*, z=-342.635*, y=47.952*, direction=125.5°*
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
  0: 0x0021 [0x1C] WAIT(180* ticks)
  1: 0x0024 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity], work=408*
  2: 0x0033 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  3: 0x0035 [0x80] LOAD_WAIT(entity=EventEntity)
  4: 0x003A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pop0" with entities [EventEntity, EventEntity], work=408*
  5: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                32 0A 80 1F 00 0B            2.....
0050: 80 0C 80 0D 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x004A [0x32] ExtData[1]->MainSpeed = 36* * 0.1
  1: 0x004D [0x1F] MOVE_ENTITY: EventEntity moves to X=338.885*, Z=-341.596*, Y=47.523*
  2: 0x0055 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0057 [0x00] END_REQSTACK()
```
