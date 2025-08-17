# 17658620 - Panta-Putta

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Abyssea - Attohwa (ID: 215) |
| Block Size       | 372 bytes                   |
| Total Events     | 7                           |
| References Count | 12                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     11 |              3 |
| [373](#event-373)        | 0x000B       |      1 |              1 |
| [65535.1](#event-655351) | 0x000C       |      6 |              2 |
| [65535.2](#event-655352) | 0x0012       |      6 |              2 |
| [65535.3](#event-655353) | 0x0018       |     77 |              9 |
| [65535.4](#event-655354) | 0x0065       |     89 |             15 |
| [65535.5](#event-655355) | 0x00BE       |     89 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0200      |         512 |
|       2 | 0x0001      |           1 |
|       3 | 0x0055      |          85 |
|       4 | 0xFFFDDD20  |  4294827296 |
|       5 | 0xFFFD40E0  |  4294787296 |
|       6 | 0x4E20      |       20000 |
|       7 | 0xFFFDE760  |  4294829920 |
|       8 | 0xFFFD8788  |  4294805384 |
|       9 | 0x04B0      |        1200 |
|      10 | 0x0100      |         256 |
|      11 | 0x1000      |        4096 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 03 00 00 00 80 03 07 00  01 80 00                 ...........     
```

#### Opcodes

```
  0: 0x0000 [0x03] ExtData[1]->WorkLocal[0] = 0*
  1: 0x0005 [0x03] ExtData[1]->WorkLocal[7] = 512*
  2: 0x000A [0x00] END_REQSTACK()
```

### Event 373

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   00                         .    
```

#### Opcodes

```
  0: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000C  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      03 00 00 02              ....
0010: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x000C [0x03] ExtData[1]->WorkLocal[0] = 1*
  1: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       03 00 00 00 80 00                             ......        
```

#### Opcodes

```
  0: 0x0012 [0x03] ExtData[1]->WorkLocal[0] = 0*
  1: 0x0017 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 77 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          5B 03 80 F8 FF FF 7F F8          [.......
0020: FF FF 7F 6A 6D 70 30 53  F8 FF FF 7F F8 FF FF 7F  ...jmp0S........
0030: 6A 6D 70 30 5B 03 80 F8  FF FF 7F F8 FF FF 7F 6A  jmp0[..........j
0040: 6D 70 30 53 F8 FF FF 7F  F8 FF FF 7F 6A 6D 70 30  mp0S........jmp0
0050: 1F 00 04 80 05 80 06 80  1F 01 1F 00 07 80 08 80  ................
0060: 06 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x0018 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "jmp0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0027 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "jmp0" with entities [EventEntity, EventEntity]
  2: 0x0034 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "jmp0" with entities [EventEntity, EventEntity], work=85*
  3: 0x0043 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "jmp0" with entities [EventEntity, EventEntity]
  4: 0x0050 [0x1F] MOVE_ENTITY: EventEntity moves to X=-140.000*, Z=-180.000*, Y=20.000*
  5: 0x0058 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x005A [0x1F] MOVE_ENTITY: EventEntity moves to X=-137.376*, Z=-161.912*, Y=20.000*
  7: 0x0062 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0064 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 89 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                3B FB 72  0D 01 01 00 03 00 02 00       ;.r........
0070: 03 04 00 01 00 03 06 00  03 00 17 01 00 07 00 09  ................
0080: 80 16 03 00 07 00 09 80  07 04 00 01 00 07 06 00  ................
0090: 03 00 1F 00 04 00 06 00  02 00 1F 01 07 07 00 0A  ................
00A0: 80 02 07 00 0B 80 02 AE  00 08 07 00 0B 80 02 00  ................
00B0: 00 02 80 00 BD 00 27 05  FC 72 0D 01 06 00        ......'..r....  
```

#### Opcodes

```
  0: 0x0065 [0x3B] GET_ENTITY_POSITION(entity=Naruru (ID: 17658619/0x010D72FB), x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[3], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x0070 [0x03] ExtData[1]->WorkLocal[4] = ExtData[1]->WorkLocal[1]
  2: 0x0075 [0x03] ExtData[1]->WorkLocal[6] = ExtData[1]->WorkLocal[3]
  3: 0x007A [0x17] ExtData[1]->WorkLocal[1] = cos(ExtData[1]->WorkLocal[7]) * 1200*
  4: 0x0081 [0x16] ExtData[1]->WorkLocal[3] = sin(ExtData[1]->WorkLocal[7]) * 1200*
  5: 0x0088 [0x07] ExtData[1]->WorkLocal[4] += ExtData[1]->WorkLocal[1]
  6: 0x008D [0x07] ExtData[1]->WorkLocal[6] += ExtData[1]->WorkLocal[3]
  7: 0x0092 [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[4], Z=ExtData[1]->WorkLocal[6], Y=ExtData[1]->WorkLocal[2]
  8: 0x009A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x009C [0x07] ExtData[1]->WorkLocal[7] += 256*
 10: 0x00A1 [0x02] IF !(ExtData[1]->WorkLocal[7] <= 4096*) GOTO 0x00AE
 11: 0x00A9 [0x08] ExtData[1]->WorkLocal[7] -= 4096*
 12: 0x00AE [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x00BD
 13: 0x00B6 [0x27] REQ_SET(priority=0x05, entity_id=Panta-Putta (ID: 17658620/0x010D72FC), tag_num=0x06)
 14: 0x00BD [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BE   |
| Data Size    | 89 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            3B FB                ;.
00C0: 72 0D 01 01 00 03 00 02  00 03 04 00 01 00 03 06  r...............
00D0: 00 03 00 17 01 00 07 00  09 80 16 03 00 07 00 09  ................
00E0: 80 07 04 00 01 00 07 06  00 03 00 1F 00 04 00 06  ................
00F0: 00 02 00 1F 01 07 07 00  0A 80 02 07 00 0B 80 02  ................
0100: 07 01 08 07 00 0B 80 02  00 00 02 80 00 16 01 27  ...............'
0110: 05 FC 72 0D 01 05 00                              ..r....         
```

#### Opcodes

```
  0: 0x00BE [0x3B] GET_ENTITY_POSITION(entity=Naruru (ID: 17658619/0x010D72FB), x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[3], z_destination=ExtData[1]->WorkLocal[2])
  1: 0x00C9 [0x03] ExtData[1]->WorkLocal[4] = ExtData[1]->WorkLocal[1]
  2: 0x00CE [0x03] ExtData[1]->WorkLocal[6] = ExtData[1]->WorkLocal[3]
  3: 0x00D3 [0x17] ExtData[1]->WorkLocal[1] = cos(ExtData[1]->WorkLocal[7]) * 1200*
  4: 0x00DA [0x16] ExtData[1]->WorkLocal[3] = sin(ExtData[1]->WorkLocal[7]) * 1200*
  5: 0x00E1 [0x07] ExtData[1]->WorkLocal[4] += ExtData[1]->WorkLocal[1]
  6: 0x00E6 [0x07] ExtData[1]->WorkLocal[6] += ExtData[1]->WorkLocal[3]
  7: 0x00EB [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[4], Z=ExtData[1]->WorkLocal[6], Y=ExtData[1]->WorkLocal[2]
  8: 0x00F3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x00F5 [0x07] ExtData[1]->WorkLocal[7] += 256*
 10: 0x00FA [0x02] IF !(ExtData[1]->WorkLocal[7] <= 4096*) GOTO 0x0107
 11: 0x0102 [0x08] ExtData[1]->WorkLocal[7] -= 4096*
 12: 0x0107 [0x02] IF !(ExtData[1]->WorkLocal[0] == 1*) GOTO 0x0116
 13: 0x010F [0x27] REQ_SET(priority=0x05, entity_id=Panta-Putta (ID: 17658620/0x010D72FC), tag_num=0x05)
 14: 0x0116 [0x00] END_REQSTACK()
```
