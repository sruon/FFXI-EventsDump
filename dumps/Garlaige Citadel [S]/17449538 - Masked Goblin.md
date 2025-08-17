# 17449538 - Masked Goblin

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Garlaige Citadel [S] (ID: 164) |
| Block Size       | 268 bytes                      |
| Total Events     | 12                             |
| References Count | 9                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [31](#event-31)          | 0x0001       |      1 |              1 |
| [32](#event-32)          | 0x0002       |      1 |              1 |
| [33](#event-33)          | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |     35 |              9 |
| [65535.2](#event-655352) | 0x0027       |     35 |              9 |
| [65535.3](#event-655353) | 0x004A       |      3 |              2 |
| [65535.4](#event-655354) | 0x004D       |      3 |              2 |
| [65535.5](#event-655355) | 0x0050       |     10 |              2 |
| [65535.6](#event-655356) | 0x005A       |     10 |              2 |
| [65535.7](#event-655357) | 0x0064       |     15 |              5 |
| [65535.8](#event-655358) | 0x0073       |     50 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x000D      |          13 |
|       2 | 0x0000      |           0 |
|       3 | 0x0001      |           1 |
|       4 | 0x0080      |         128 |
|       5 | 0xFFFFE2C0  |  4294959808 |
|       6 | 0xFFFBA165  |  4294680933 |
|       7 | 0x005B      |          91 |
|       8 | 0x00DA      |         218 |

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

### Event 31

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             03 00 00 25  10 03 02 00 27 10 03 01      ...%....'...
0010: 00 26 10 03 03 00 28 10  32 00 80 1F 00 00 00 02  .&....(.2.......
0020: 00 01 00 1F 01 6F 00                              .....o.         
```

#### Opcodes

```
  0: 0x0004 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x0009 [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x000E [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0013 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x0018 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  5: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0025 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      03  00 00 25 10 03 02 00 27         ...%....'
0030: 10 03 01 00 26 10 03 03  00 28 10 32 01 80 1F 00  ....&....(.2....
0040: 00 00 02 00 01 00 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x0027 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x002C [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x0031 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0036 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x003B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0048 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004A  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                33 01 00                     3..   
```

#### Opcodes

```
  0: 0x004A [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004D  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         33 00 00               3..
```

#### Opcodes

```
  0: 0x004D [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  1: 0x004F [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0050   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050: 6C F8 FF FF 7F 02 80 03  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0050 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                6C F8 FF FF 7F 04            l.....
0060: 80 03 80 00                                       ....            
```

#### Opcodes

```
  0: 0x005A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             32 00 80 1F  00 05 80 06 80 07 80 1F      2...........
0070: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0064 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0067 [0x1F] MOVE_ENTITY: EventEntity moves to X=-7.488*, Z=-286.363*, Y=0.091*
  2: 0x006F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0071 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 50 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          32 00 80 1F 00  05 80 06 80 07 80 1F 01     2............
0080: 6F 4A 42 42 0A 01 1B 42  0A 01 7B 42 42 0A 01 6F  oJBB...B..{BB..o
0090: 76 42 42 0A 01 5B 08 80  42 42 0A 01 42 42 0A 01  vBB..[..BB..BB..
00A0: 63 6F 6D 30 00                                    com0.           
```

#### Opcodes

```
  0: 0x0073 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0076 [0x1F] MOVE_ENTITY: EventEntity moves to X=-7.488*, Z=-286.363*, Y=0.091*
  2: 0x007E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0080 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0081 [0x4A] Masked Goblin (ID: 17449538/0x010A4242) looks at Mitillie (ID: 17449499/0x010A421B)
  5: 0x008A [0x7B] Masked Goblin (ID: 17449538/0x010A4242) stops talking
  6: 0x008F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x0090 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Masked Goblin (ID: 17449538/0x010A4242) Render.Flags0 and Render.Flags3 conditions are met
  8: 0x0095 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "com0" with entities [Masked Goblin (ID: 17449538/0x010A4242), Masked Goblin (ID: 17449538/0x010A4242)], work=218*
  9: 0x00A4 [0x00] END_REQSTACK()
```
