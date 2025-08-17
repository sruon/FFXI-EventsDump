# 17744019 - Gueravrel

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Port Bastok (ID: 236) |
| Block Size       | 200 bytes             |
| Total Events     | 8                     |
| References Count | 14                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     35 |              7 |
| [270](#event-270)        | 0x0024       |      1 |              1 |
| [65535.2](#event-655352) | 0x0025       |     26 |              6 |
| [65535.3](#event-655353) | 0x003F       |     14 |              4 |
| [65535.4](#event-655354) | 0x004D       |     16 |              5 |
| [272](#event-272)        | 0x005D       |      1 |              1 |
| [274](#event-274)        | 0x005E       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFDD634  |  4294825524 |
|       1 | 0x2216      |        8726 |
|       2 | 0xFFFFE2C8  |  4294959816 |
|       3 | 0x09E0      |        2528 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFDC821  |  4294821921 |
|       6 | 0x2AED      |       10989 |
|       7 | 0xFFFDC086  |  4294819974 |
|       8 | 0x28DC      |       10460 |
|       9 | 0xFFFDB963  |  4294818147 |
|      10 | 0x293A      |       10554 |
|      11 | 0xFFFDA831  |  4294813745 |
|      12 | 0x1B3C      |        6972 |
|      13 | 0xFFFFE2B8  |  4294959800 |

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 35 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 22 00 32 04 80 1F   7........".2...
0010: 00 05 80 06 80 02 80 1F  01 79 00 F8 FF FF 7F 0C  .........y......
0020: C0 0E 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-141.772*, z=8.726*, y=-7.480*, direction=222.2°*
  1: 0x000A [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  2: 0x000C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-145.375*, Z=10.989*, Y=-7.480*
  4: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0019 [0x79] EventEntity looks at Carmelo (ID: 17743884/0x010EC00C) (Basic look)
  6: 0x0023 [0x00] END_REQSTACK()
```

### Event 270

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0024  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             00                                        .           
```

#### Opcodes

```
  0: 0x0024 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0025   |
| Data Size    | 26 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                22 00 32  04 80 1F 00 07 80 08 80       ".2........
0030: 02 80 1F 01 79 00 F8 FF  FF 7F 0C C0 0E 01 00     ....y.......... 
```

#### Opcodes

```
  0: 0x0025 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0027 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x002A [0x1F] MOVE_ENTITY: EventEntity moves to X=-147.322*, Z=10.460*, Y=-7.480*
  3: 0x0032 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0034 [0x79] EventEntity looks at Carmelo (ID: 17743884/0x010EC00C) (Basic look)
  5: 0x003E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003F   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                               32                 2
0040: 04 80 1F 00 09 80 0A 80  02 80 1F 01 00           .............   
```

#### Opcodes

```
  0: 0x003F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0042 [0x1F] MOVE_ENTITY: EventEntity moves to X=-149.149*, Z=10.554*, Y=-7.480*
  2: 0x004A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         32 04 80               2..
0050: 1F 00 0B 80 0C 80 0D 80  1F 01 22 01 00           .........."..   
```

#### Opcodes

```
  0: 0x004D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0050 [0x1F] MOVE_ENTITY: EventEntity moves to X=-153.551*, Z=6.972*, Y=-7.496*
  2: 0x0058 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x005A [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x005C [0x00] END_REQSTACK()
```

### Event 272

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         00                     .  
```

#### Opcodes

```
  0: 0x005D [0x00] END_REQSTACK()
```

### Event 274

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            00                   . 
```

#### Opcodes

```
  0: 0x005E [0x00] END_REQSTACK()
```
