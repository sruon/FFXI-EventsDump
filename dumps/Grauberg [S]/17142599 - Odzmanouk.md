# 17142599 - Odzmanouk

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Grauberg [S] (ID: 89) |
| Block Size       | 368 bytes             |
| Total Events     | 11                    |
| References Count | 27                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [17](#event-17)          | 0x0001       |      3 |              2 |
| [18](#event-18)          | 0x0004       |      3 |              2 |
| [65535.1](#event-655351) | 0x0007       |      4 |              2 |
| [65535.2](#event-655352) | 0x000B       |      2 |              2 |
| [65535.3](#event-655353) | 0x000D       |      3 |              2 |
| [65535.4](#event-655354) | 0x0010       |      3 |              2 |
| [65535.5](#event-655355) | 0x0013       |     58 |             11 |
| [65535.6](#event-655356) | 0x004D       |     58 |             11 |
| [65535.7](#event-655357) | 0x0087       |     58 |             11 |
| [65535.8](#event-655358) | 0x00C1       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0002      |           2 |
|       1 | 0xFFFD38F3  |  4294785267 |
|       2 | 0xFFFA65EB  |  4294600171 |
|       3 | 0xFFFF7749  |  4294932297 |
|       4 | 0xFFFDCAC5  |  4294822597 |
|       5 | 0x00D2      |         210 |
|       6 | 0x0118      |         280 |
|       7 | 0x0055      |          85 |
|       8 | 0x0D84      |        3460 |
|       9 | 0x0001      |           1 |
|      10 | 0xFFFDBF56  |  4294819670 |
|      11 | 0xFFFADF08  |  4294631176 |
|      12 | 0xFFFF6119  |  4294926617 |
|      13 | 0x0000      |           0 |
|      14 | 0x01CE      |         462 |
|      15 | 0x00E7      |         231 |
|      16 | 0x0019      |          25 |
|      17 | 0x0E06      |        3590 |
|      18 | 0x14A1F     |       84511 |
|      19 | 0xFFFCF918  |  4294768920 |
|      20 | 0xFFFEB33F  |  4294882111 |
|      21 | 0x1ADB0     |      110000 |
|      22 | 0x014D      |         333 |
|      23 | 0x01BC      |         444 |
|      24 | 0x0096      |         150 |
|      25 | 0x0DAC      |        3500 |
|      26 | 0x0032      |          50 |

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

### Event 17

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

### Event 18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0004  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             33 01 00                                  3..         
```

#### Opcodes

```
  0: 0x0004 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0006 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0007  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                      95  00 80 00                        ....     
```

#### Opcodes

```
  0: 0x0007 [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 2*)
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000B  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   96 00                      ..   
```

#### Opcodes

```
  0: 0x000B [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x000C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         A4 01 00               ...
```

#### Opcodes

```
  0: 0x000D [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  1: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0010  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: A4 00 00                                          ...             
```

#### Opcodes

```
  0: 0x0010 [0xA4] EventEntity->Flags3.unknown_3_2 = 0
  1: 0x0012 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 58 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          03 00 00 01 80  03 01 00 02 80 03 02 00     .............
0020: 03 80 02 00 00 04 80 03  4C 00 07 00 00 05 80 07  ........L.......
0030: 01 00 06 80 07 02 00 07  80 BA 47 93 05 01 00 00  ..........G.....
0040: 01 00 02 00 08 80 1C 09  80 01 22 00 00           .........."..   
```

#### Opcodes

```
  0: 0x0013 [0x03] ExtData[1]->WorkLocal[0] = 4294785267*
  1: 0x0018 [0x03] ExtData[1]->WorkLocal[1] = 4294600171*
  2: 0x001D [0x03] ExtData[1]->WorkLocal[2] = 4294932297*
  3: 0x0022 [0x02] IF !(ExtData[1]->WorkLocal[0] >= 4294822597*) GOTO 0x004C
  4: 0x002A [0x07] ExtData[1]->WorkLocal[0] += 210*
  5: 0x002F [0x07] ExtData[1]->WorkLocal[1] += 280*
  6: 0x0034 [0x07] ExtData[1]->WorkLocal[2] += 85*
  7: 0x0039 [0xBA] SET_ENTITY_POSITION(entity_id=Odzmanouk (ID: 17142599/0x01059347), pos_x=ExtData[1]->WorkLocal[0], pos_z=ExtData[1]->WorkLocal[1], pos_y=ExtData[1]->WorkLocal[2], direction=304.1°*)
  8: 0x0046 [0x1C] WAIT(1* ticks)
  9: 0x0049 [0x01] GOTO 0x0022
 10: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004D   |
| Data Size    | 58 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         03 00 00               ...
0050: 0A 80 03 01 00 0B 80 03  02 00 0C 80 02 00 00 0D  ................
0060: 80 03 86 00 07 00 00 0E  80 07 01 00 0F 80 08 02  ................
0070: 00 10 80 BA 47 93 05 01  00 00 01 00 02 00 11 80  ....G...........
0080: 1C 09 80 01 5C 00 00                              ....\..         
```

#### Opcodes

```
  0: 0x004D [0x03] ExtData[1]->WorkLocal[0] = 4294819670*
  1: 0x0052 [0x03] ExtData[1]->WorkLocal[1] = 4294631176*
  2: 0x0057 [0x03] ExtData[1]->WorkLocal[2] = 4294926617*
  3: 0x005C [0x02] IF !(ExtData[1]->WorkLocal[0] >= 0*) GOTO 0x0086
  4: 0x0064 [0x07] ExtData[1]->WorkLocal[0] += 462*
  5: 0x0069 [0x07] ExtData[1]->WorkLocal[1] += 231*
  6: 0x006E [0x08] ExtData[1]->WorkLocal[2] -= 25*
  7: 0x0073 [0xBA] SET_ENTITY_POSITION(entity_id=Odzmanouk (ID: 17142599/0x01059347), pos_x=ExtData[1]->WorkLocal[0], pos_z=ExtData[1]->WorkLocal[1], pos_y=ExtData[1]->WorkLocal[2], direction=315.5°*)
  8: 0x0080 [0x1C] WAIT(1* ticks)
  9: 0x0083 [0x01] GOTO 0x005C
 10: 0x0086 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0087   |
| Data Size    | 58 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                      03  00 00 12 80 03 01 00 13         .........
0090: 80 03 02 00 14 80 02 00  00 15 80 03 C0 00 07 00  ................
00A0: 00 16 80 07 01 00 17 80  07 02 00 18 80 BA 47 93  ..............G.
00B0: 05 01 00 00 01 00 02 00  19 80 1C 09 80 01 96 00  ................
00C0: 00                                                .               
```

#### Opcodes

```
  0: 0x0087 [0x03] ExtData[1]->WorkLocal[0] = 84511*
  1: 0x008C [0x03] ExtData[1]->WorkLocal[1] = 4294768920*
  2: 0x0091 [0x03] ExtData[1]->WorkLocal[2] = 4294882111*
  3: 0x0096 [0x02] IF !(ExtData[1]->WorkLocal[0] >= 110000*) GOTO 0x00C0
  4: 0x009E [0x07] ExtData[1]->WorkLocal[0] += 333*
  5: 0x00A3 [0x07] ExtData[1]->WorkLocal[1] += 444*
  6: 0x00A8 [0x07] ExtData[1]->WorkLocal[2] += 150*
  7: 0x00AD [0xBA] SET_ENTITY_POSITION(entity_id=Odzmanouk (ID: 17142599/0x01059347), pos_x=ExtData[1]->WorkLocal[0], pos_z=ExtData[1]->WorkLocal[1], pos_y=ExtData[1]->WorkLocal[2], direction=307.6°*)
  8: 0x00BA [0x1C] WAIT(1* ticks)
  9: 0x00BD [0x01] GOTO 0x0096
 10: 0x00C0 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C1  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:    39 1A 80 00                                     9...           
```

#### Opcodes

```
  0: 0x00C1 [0x39] SET_ENTITY_DIRECTION(direction=0.3°*)
  1: 0x00C4 [0x00] END_REQSTACK()
```
