# 17122233 - Cait Sith Naoi

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Batallia Downs [S] (ID: 84) |
| Block Size       | 204 bytes                   |
| Total Events     | 7                           |
| References Count | 10                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [21](#event-21)          | 0x0001       |      3 |              2 |
| [65535.1](#event-655351) | 0x0004       |     28 |              7 |
| [65535.2](#event-655352) | 0x0020       |     67 |             13 |
| [65535.3](#event-655353) | 0x0063       |      8 |              3 |
| [65535.4](#event-655354) | 0x006B       |      6 |              3 |
| [22](#event-22)          | 0x0071       |      7 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0BB1      |        2993 |
|       1 | 0x0271      |         625 |
|       2 | 0x0020      |          32 |
|       3 | 0x0001      |           1 |
|       4 | 0x0003      |           3 |
|       5 | 0x0040      |          64 |
|       6 | 0x0800      |        2048 |
|       7 | 0x08F1      |        2289 |
|       8 | 0x0002      |           2 |
|       9 | 0x08CF      |        2255 |

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

### Event 21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    33 01 00                                        3..            
```

#### Opcodes

```
  0: 0x0001 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 28 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             03 00 00 00  80 02 00 00 01 80 01 1F      ............
0010: 00 08 00 00 02 80 39 00  00 1C 03 80 01 09 00 00  ......9.........
```

#### Opcodes

```
  0: 0x0004 [0x03] ExtData[1]->WorkLocal[0] = 2993*
  1: 0x0009 [0x02] IF !(ExtData[1]->WorkLocal[0] == 625*) GOTO 0x001F
  2: 0x0011 [0x08] ExtData[1]->WorkLocal[0] -= 32*
  3: 0x0016 [0x39] SET_ENTITY_DIRECTION(direction=ExtData[1]->WorkLocal[0])
  4: 0x0019 [0x1C] WAIT(1* ticks)
  5: 0x001C [0x01] GOTO 0x0009
  6: 0x001F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0020   |
| Data Size    | 67 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020: 33 01 3B F8 FF FF 7F 01  00 02 00 03 00 06 06 00  3.;.............
0030: 16 05 00 06 00 04 80 07  03 00 05 00 3A F8 FF FF  ............:...
0040: 7F 04 00 37 01 00 02 00  03 00 04 00 07 06 00 05  ...7............
0050: 80 1C 03 80 01 30 00 02  06 00 06 80 04 62 00 06  .....0.......b..
0060: 06 00 00                                          ...             
```

#### Opcodes

```
  0: 0x0020 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0022 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
  2: 0x002D [0x06] ExtData[1]->WorkLocal[6] = 0
  3: 0x0030 [0x16] ExtData[1]->WorkLocal[5] = sin(ExtData[1]->WorkLocal[6]) * 3*
  4: 0x0037 [0x07] ExtData[1]->WorkLocal[3] += ExtData[1]->WorkLocal[5]
  5: 0x003C [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
  6: 0x0043 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[1], z=ExtData[1]->WorkLocal[2], y=ExtData[1]->WorkLocal[3], direction=ExtData[1]->WorkLocal[4]
  7: 0x004C [0x07] ExtData[1]->WorkLocal[6] += 64*
  8: 0x0051 [0x1C] WAIT(1* ticks)
  9: 0x0054 [0x01] GOTO 0x0030
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0057 [0x02] IF !(ExtData[1]->WorkLocal[6] < 2048*) GOTO 0x0062
     0x005F [0x06] ExtData[1]->WorkLocal[6] = 0
     0x0062 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 8 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          B6 00 07 80 95  08 80 00                    ........     
```

#### Opcodes

```
  0: 0x0063 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2289*)
  1: 0x0067 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 2*)
  2: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006B  |
| Data Size    | 6 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   B6 00 09 80 96             .....
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x006B [0xB6] ENTITY_APPEARANCE_HANDLER(case=Hair style, value=2255*)
  1: 0x006F [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  2: 0x0070 [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0071  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0071 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0077 [0x00] END_REQSTACK()
```
