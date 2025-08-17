# 17056433 - Mihli Aliapoh

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Aydeewa Subterrane (ID: 68) |
| Block Size       | 528 bytes                   |
| Total Events     | 20                          |
| References Count | 37                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [34](#event-34)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     21 |              2 |
| [65535.2](#event-655352)   | 0x0017       |     21 |              2 |
| [65535.3](#event-655353)   | 0x002C       |     20 |              6 |
| [65535.4](#event-655354)   | 0x0040       |     20 |              6 |
| [65535.5](#event-655355)   | 0x0054       |     15 |              5 |
| [65535.6](#event-655356)   | 0x0063       |     10 |              2 |
| [65535.7](#event-655357)   | 0x006D       |     10 |              2 |
| [65535.8](#event-655358)   | 0x0077       |     15 |              5 |
| [65535.9](#event-655359)   | 0x0086       |     20 |              6 |
| [65535.10](#event-6553510) | 0x009A       |     26 |              8 |
| [65535.11](#event-6553511) | 0x00B4       |     21 |              2 |
| [65535.12](#event-6553512) | 0x00C9       |     10 |              2 |
| [65535.13](#event-6553513) | 0x00D3       |     10 |              2 |
| [65535.14](#event-6553514) | 0x00DD       |     21 |              2 |
| [65535.15](#event-6553515) | 0x00F2       |     12 |              3 |
| [65535.16](#event-6553516) | 0x00FE       |     21 |              2 |
| [65535.17](#event-6553517) | 0x0113       |      4 |              2 |
| [65535.18](#event-6553518) | 0x0117       |      4 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0007      |           7 |
|       1 | 0x000D      |          13 |
|       2 | 0x00AE      |         174 |
|       3 | 0x0083      |         131 |
|       4 | 0x0000      |           0 |
|       5 | 0x00AF      |         175 |
|       6 | 0x00A7      |         167 |
|       7 | 0x000B      |          11 |
|       8 | 0x13275     |       78453 |
|       9 | 0xD899      |       55449 |
|      10 | 0xFFFFFEC5  |  4294966981 |
|      11 | 0x13230     |       78384 |
|      12 | 0xC794      |       51092 |
|      13 | 0x01E0      |         480 |
|      14 | 0x0028      |          40 |
|      15 | 0x136E8     |       79592 |
|      16 | 0x02B5      |         693 |
|      17 | 0x000F      |          15 |
|      18 | 0x0080      |         128 |
|      19 | 0x0032      |          50 |
|      20 | 0x263A      |        9786 |
|      21 | 0xB734      |       46900 |
|      22 | 0x211E      |        8478 |
|      23 | 0xAE53      |       44627 |
|      24 | 0x0024      |          36 |
|      25 | 0x1A46      |        6726 |
|      26 | 0xCFB6      |       53174 |
|      27 | 0x0537      |        1335 |
|      28 | 0xE898      |       59544 |
|      29 | 0x006F      |         111 |
|      30 | 0x0020      |          32 |
|      31 | 0x0005      |           5 |
|      32 | 0x12951     |       76113 |
|      33 | 0x3E15      |       15893 |
|      34 | 0xFFFFFF9C  |  4294967196 |
|      35 | 0x0400      |        1024 |
|      36 | 0x0001      |           1 |

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

### Event 34

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       B6 0B 00 80 01 80  02 80 03 80 03 80 03 80    ..............
0010: 03 80 04 80 04 80 00                              .......         
```

#### Opcodes

```
  0: 0x0002 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=13*, head=174*, body=131*, hands=131*, legs=131*, feet=131*, main=0*, sub=0*)
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      B6  0B 00 80 01 80 05 80 05         .........
0020: 80 05 80 05 80 05 80 06  80 06 80 00              ............    
```

#### Opcodes

```
  0: 0x0017 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=13*, head=175*, body=175*, hands=175*, legs=175*, feet=175*, main=167*, sub=167*)
  1: 0x002B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002C   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                      32 07 80 1F              2...
0030: 00 08 80 09 80 0A 80 1F  01 6F 1E B4 42 04 01 00  .........o..B...
```

#### Opcodes

```
  0: 0x002C [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=78.453*, Z=55.449*, Y=-0.315*
  2: 0x0037 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0039 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x003A [0x1E] EventEntity looks at Aphmau (ID: 17056436/0x010442B4) and starts talking
  5: 0x003F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0040   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040: 32 07 80 1F 00 0B 80 0C  80 0D 80 1F 01 6F 1E B4  2............o..
0050: 42 04 01 00                                       B...            
```

#### Opcodes

```
  0: 0x0040 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0043 [0x1F] MOVE_ENTITY: EventEntity moves to X=78.384*, Z=51.092*, Y=0.480*
  2: 0x004B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004E [0x1E] EventEntity looks at Aphmau (ID: 17056436/0x010442B4) and starts talking
  5: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             32 0E 80 1F  00 0F 80 10 80 04 80 1F      2...........
0060: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0054 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0057 [0x1F] MOVE_ENTITY: EventEntity moves to X=79.592*, Z=0.693*, Y=0.000*
  2: 0x005F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0061 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          6C F8 FF FF 7F  04 80 11 80 00              l.........   
```

#### Opcodes

```
  0: 0x0063 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=15*)
  1: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         6C F8 FF               l..
0070: FF 7F 12 80 13 80 00                              .......         
```

#### Opcodes

```
  0: 0x006D [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=50*)
  1: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      32  01 80 1F 00 14 80 15 80         2........
0080: 04 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0077 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x007A [0x1F] MOVE_ENTITY: EventEntity moves to X=9.786*, Z=46.900*, Y=0.000*
  2: 0x0082 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0084 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   32 07  80 1F 00 16 80 17 80 04        2.........
0090: 80 1F 01 6F 1E C1 42 04  01 00                    ...o..B...      
```

#### Opcodes

```
  0: 0x0086 [0x32] ExtData[1]->MainSpeed = 11* * 0.1
  1: 0x0089 [0x1F] MOVE_ENTITY: EventEntity moves to X=8.478*, Z=44.627*, Y=0.000*
  2: 0x0091 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0093 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0094 [0x1E] EventEntity looks at Khio Lezengha (ID: 17056449/0x010442C1) and starts talking
  5: 0x0099 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009A   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                32 18 80 1F 00 19            2.....
00A0: 80 1A 80 04 80 1F 01 6F  1F 00 1B 80 1C 80 04 80  .......o........
00B0: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x009A [0x32] ExtData[1]->MainSpeed = 36* * 0.1
  1: 0x009D [0x1F] MOVE_ENTITY: EventEntity moves to X=6.726*, Z=53.174*, Y=0.000*
  2: 0x00A5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A7 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00A8 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.335*, Z=59.544*, Y=0.000*
  5: 0x00B0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x00B2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x00B3 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B4   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             B6 0B 00 80  01 80 05 80 05 80 05 80      ............
00C0: 05 80 05 80 1D 80 1E 80  00                       .........       
```

#### Opcodes

```
  0: 0x00B4 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=13*, head=175*, body=175*, hands=175*, legs=175*, feet=175*, main=111*, sub=32*)
  1: 0x00C8 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C9   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                             6C F8 FF FF 7F 04 80           l......
00D0: 04 80 00                                          ...             
```

#### Opcodes

```
  0: 0x00C9 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=0*)
  1: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          6C F8 FF FF 7F  12 80 1F 80 00              l.........   
```

#### Opcodes

```
  0: 0x00D3 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=5*)
  1: 0x00DC [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DD   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                         B6 0B 00               ...
00E0: 80 01 80 05 80 05 80 05  80 05 80 05 80 04 80 04  ................
00F0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x00DD [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=13*, head=175*, body=175*, hands=175*, legs=175*, feet=175*, main=0*, sub=0*)
  1: 0x00F1 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F2   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:       33 01 37 20 80 21  80 22 80 23 80 00          3.7 .!.".#..  
```

#### Opcodes

```
  0: 0x00F2 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x00F4 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=76.113*, z=15.893*, y=-0.100*, direction=90.0°*
  2: 0x00FD [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FE   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                            B6 0B                ..
0100: 00 80 01 80 05 80 05 80  05 80 05 80 05 80 06 80  ................
0110: 04 80 00                                          ...             
```

#### Opcodes

```
  0: 0x00FE [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=7*, hair=13*, head=175*, body=175*, hands=175*, legs=175*, feet=175*, main=167*, sub=0*)
  1: 0x0112 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0113  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:          C0 24 80 00                                 .$..         
```

#### Opcodes

```
  0: 0x0113 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  1: 0x0116 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0117  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                      C0  04 80 00                        ....     
```

#### Opcodes

```
  0: 0x0117 [0xC0] EventEntity->Render.Flags3 &= ~0x1000 // Clear bit 12 (from 0*)
  1: 0x011A [0x00] END_REQSTACK()
```
