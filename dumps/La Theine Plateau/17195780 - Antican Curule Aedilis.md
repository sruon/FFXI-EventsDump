# 17195780 - Antican Curule Aedilis

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | La Theine Plateau (ID: 102) |
| Block Size       | 304 bytes                   |
| Total Events     | 10                          |
| References Count | 20                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [225](#event-225)        | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     65 |             11 |
| [65535.2](#event-655352) | 0x0049       |      6 |              2 |
| [226](#event-226)        | 0x004F       |      7 |              2 |
| [227](#event-227)        | 0x0056       |      7 |              2 |
| [65535.3](#event-655353) | 0x005D       |      7 |              3 |
| [65535.4](#event-655354) | 0x0064       |      7 |              3 |
| [65535.5](#event-655355) | 0x006B       |     15 |              5 |
| [65535.6](#event-655356) | 0x007A       |     44 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x001E      |          30 |
|       2 | 0x006E      |         110 |
|       3 | 0x0001      |           1 |
|       4 | 0x000D      |          13 |
|       5 | 0x3C206     |      246278 |
|       6 | 0xFFFAA25C  |  4294615644 |
|       7 | 0x4EFB      |       20219 |
|       8 | 0x3C273     |      246387 |
|       9 | 0xFFFAA7F3  |  4294617075 |
|      10 | 0x4E72      |       20082 |
|      11 | 0x3BCDF     |      244959 |
|      12 | 0xFFFAC152  |  4294623570 |
|      13 | 0x4EDE      |       20190 |
|      14 | 0x3B5F8     |      243192 |
|      15 | 0xFFFADCC8  |  4294630600 |
|      16 | 0x50B8      |       20664 |
|      17 | 0x3AE1D     |      241181 |
|      18 | 0xFFFAF645  |  4294637125 |
|      19 | 0x5023      |       20515 |

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

### Event 225

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 65 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          03 00 00 00 80 02 00 00          ........
0010: 00 80 00 48 00 1C 01 80  C4 01 00 80 F8 FF FF 7F  ...H............
0020: FE 62 06 01 1C 02 80 C4  01 00 80 F8 FF FF 7F FE  .b..............
0030: 62 06 01 1C 02 80 C4 01  00 80 F8 FF FF 7F FE 62  b..............b
0040: 06 01 1C 02 80 01 0D 00  00                       .........       
```

#### Opcodes

```
  0: 0x0008 [0x03] ExtData[1]->WorkLocal[0] = 0*
  1: 0x000D [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0048
  2: 0x0015 [0x1C] WAIT(30* ticks)
  3: 0x0018 [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=17): EventEntity casts magic 0* on Kupofried (ID: 17195774/0x010662FE)
  4: 0x0024 [0x1C] WAIT(110* ticks)
  5: 0x0027 [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=17): EventEntity casts magic 0* on Kupofried (ID: 17195774/0x010662FE)
  6: 0x0033 [0x1C] WAIT(110* ticks)
  7: 0x0036 [0xC4] SCHEDULE_MAGIC_CASTING_ALT (arg=17): EventEntity casts magic 0* on Kupofried (ID: 17195774/0x010662FE)
  8: 0x0042 [0x1C] WAIT(110* ticks)
  9: 0x0045 [0x01] GOTO 0x000D
 10: 0x0048 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0049  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                             03 00 00 03 80 00              ...... 
```

#### Opcodes

```
  0: 0x0049 [0x03] ExtData[1]->WorkLocal[0] = 1*
  1: 0x004E [0x00] END_REQSTACK()
```

### Event 226

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                               92                 .
0050: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x004F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0055 [0x00] END_REQSTACK()
```

### Event 227

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0056  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0056 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x005C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005D  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         AB 03 AC               ...
0060: 01 03 80 00                                       ....            
```

#### Opcodes

```
  0: 0x005D [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x005F [0xAC] EventEntity->StatusEvent = 1*
  2: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             AC 01 00 80  AB 04 00                     .......     
```

#### Opcodes

```
  0: 0x0064 [0xAC] EventEntity->StatusEvent = 0*
  1: 0x0068 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x006A [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                   32 04 80 1F 00             2....
0070: 05 80 06 80 07 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x006B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x006E [0x1F] MOVE_ENTITY: EventEntity moves to X=246.278*, Z=-351.652*, Y=20.219*
  2: 0x0076 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0078 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0079 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007A   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                32 04 80 5A 00 08            2..Z..
0080: 80 09 80 0A 80 5A 01 5A  00 0B 80 0C 80 0D 80 5A  .....Z.Z.......Z
0090: 01 5A 00 0E 80 0F 80 10  80 5A 01 5A 00 11 80 12  .Z.......Z.Z....
00A0: 80 13 80 5A 01 00                                 ...Z..          
```

#### Opcodes

```
  0: 0x007A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007D [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=246.387*, Z=-350.221*, Y=20.082*
  2: 0x0085 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0087 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=244.959*, Z=-343.726*, Y=20.190*
  4: 0x008F [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  5: 0x0091 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=243.192*, Z=-336.696*, Y=20.664*
  6: 0x0099 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  7: 0x009B [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=241.181*, Z=-330.171*, Y=20.515*
  8: 0x00A3 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  9: 0x00A5 [0x00] END_REQSTACK()
```
