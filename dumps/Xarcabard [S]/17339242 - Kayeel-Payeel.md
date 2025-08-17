# 17339242 - Kayeel-Payeel

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Xarcabard [S] (ID: 137) |
| Block Size       | 432 bytes               |
| Total Events     | 18                      |
| References Count | 28                      |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0001       |      1 |              1 |
| [65535.2](#event-655352)   | 0x0002       |     18 |              4 |
| [65535.3](#event-655353)   | 0x0014       |     10 |              2 |
| [65535.4](#event-655354)   | 0x001E       |      9 |              3 |
| [65535.5](#event-655355)   | 0x0027       |      9 |              3 |
| [65535.6](#event-655356)   | 0x0030       |     10 |              2 |
| [65535.7](#event-655357)   | 0x003A       |     10 |              2 |
| [65535.8](#event-655358)   | 0x0044       |     13 |              3 |
| [65535.9](#event-655359)   | 0x0051       |     40 |              9 |
| [65535.10](#event-6553510) | 0x0079       |     16 |              4 |
| [65535.11](#event-6553511) | 0x0089       |     16 |              2 |
| [65535.12](#event-6553512) | 0x0099       |     29 |              6 |
| [21](#event-21)            | 0x00B6       |      1 |              1 |
| [22](#event-22)            | 0x00B7       |      1 |              1 |
| [25](#event-25)            | 0x00B8       |      1 |              1 |
| [65535.13](#event-6553513) | 0x00B9       |     15 |              5 |
| [65535.14](#event-6553514) | 0x00C8       |     31 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x0013      |          19 |
|       4 | 0x000D      |          13 |
|       5 | 0xE999      |       59801 |
|       6 | 0xFFFCAF4A  |  4294750026 |
|       7 | 0xFFFFA274  |  4294943348 |
|       8 | 0xE184      |       57732 |
|       9 | 0xFFFCAFC4  |  4294750148 |
|      10 | 0xFFFFA2B1  |  4294943409 |
|      11 | 0xDC4A      |       56394 |
|      12 | 0xFFFCB15E  |  4294750558 |
|      13 | 0xFFFFA2F3  |  4294943475 |
|      14 | 0x0019      |          25 |
|      15 | 0x00B4      |         180 |
|      16 | 0x0028      |          40 |
|      17 | 0xF33D      |       62269 |
|      18 | 0xFFFCAB3D  |  4294748989 |
|      19 | 0xFFFFA2E9  |  4294943465 |
|      20 | 0xE2E7      |       58087 |
|      21 | 0xFFFCAC50  |  4294749264 |
|      22 | 0xFFFFA29F  |  4294943391 |
|      23 | 0xEF21      |       61217 |
|      24 | 0xFFFCB246  |  4294750790 |
|      25 | 0xFFFFA295  |  4294943381 |
|      26 | 0x000A      |          10 |
|      27 | 0x0696      |        1686 |

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

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 18 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 00 2F 00 F8 FF  FF 7F 6C F8 FF FF 7F 00    "./.....l.....
0010: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0004 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  3: 0x0013 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0014   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:             6C F8 FF FF  7F 02 80 01 80 00            l.........  
```

#### Opcodes

```
  0: 0x0014 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            22 00                ".
0020: 2F 00 F8 FF FF 7F 00                              /......         
```

#### Opcodes

```
  0: 0x001E [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0020 [0x2F] EventEntity->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      22  01 2F 01 F8 FF FF 7F 00         "./......
```

#### Opcodes

```
  0: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0029 [0x2F] EventEntity->Render.Flags0 |= 0x80000 // Bit 19
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 6C F8 FF FF 7F 00 80 01  80 00                    l.........      
```

#### Opcodes

```
  0: 0x0030 [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=0*, fade_time=1*)
  1: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00                                       ....            
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0044   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:             6E F8 FF FF  7F 03 80 99 F8 FF FF 7F      n...........
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0044 [0x6E] EventEntity uses emote 19*
  1: 0x004B [0x99] Wait for EventEntity animation to complete
  2: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 40 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    59 04 F8 FF FF 7F 04  80 1F 00 05 80 06 80 07   Y..............
0060: 80 1F 01 1F 00 08 80 09  80 0A 80 1F 01 1F 00 0B  ................
0070: 80 0C 80 0D 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x0051 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x0059 [0x1F] MOVE_ENTITY: EventEntity moves to X=59.801*, Z=-217.270*, Y=-23.948*
  2: 0x0061 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0063 [0x1F] MOVE_ENTITY: EventEntity moves to X=57.732*, Z=-217.148*, Y=-23.887*
  4: 0x006B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x006D [0x1F] MOVE_ENTITY: EventEntity moves to X=56.394*, Z=-216.738*, Y=-23.821*
  6: 0x0075 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0077 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0078 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0079   |
| Data Size    | 16 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                             6E F8 FF FF 7F 0E 80           n......
0080: 99 F8 FF FF 7F 1C 0F 80  00                       .........       
```

#### Opcodes

```
  0: 0x0079 [0x6E] EventEntity uses emote 25*
  1: 0x0080 [0x99] Wait for EventEntity animation to complete
  2: 0x0085 [0x1C] WAIT(180* ticks)
  3: 0x0088 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0089   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                             66 10 80 F8 FF FF 7F           f......
0090: F8 FF FF 7F 67 6B 72 30  00                       ....gkr0.       
```

#### Opcodes

```
  0: 0x0089 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "gkr0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 29 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             59 04 F8 FF FF 7F 04           Y......
00A0: 80 1F 00 11 80 12 80 13  80 1F 01 6F 4A F8 FF FF  ...........oJ...
00B0: 7F F0 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x0099 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x00A1 [0x1F] MOVE_ENTITY: EventEntity moves to X=62.269*, Z=-218.307*, Y=-23.831*
  2: 0x00A9 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00AB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00AC [0x4A] EventEntity looks at LocalPlayer
  5: 0x00B5 [0x00] END_REQSTACK()
```

### Event 21

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                   00                                    .         
```

#### Opcodes

```
  0: 0x00B6 [0x00] END_REQSTACK()
```

### Event 22

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B7  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                      00                                  .        
```

#### Opcodes

```
  0: 0x00B7 [0x00] END_REQSTACK()
```

### Event 25

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                          00                               .       
```

#### Opcodes

```
  0: 0x00B8 [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             32 04 80 1F 00 14 80           2......
00C0: 15 80 16 80 1F 01 6F 00                           ......o.        
```

#### Opcodes

```
  0: 0x00B9 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00BC [0x1F] MOVE_ENTITY: EventEntity moves to X=58.087*, Z=-218.032*, Y=-23.905*
  2: 0x00C4 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C6 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00C7 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C8   |
| Data Size    | 31 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                          32 04 80 1F 00 17 80 18          2.......
00D0: 80 19 80 1F 01 6F 1C 1A  80 4B F8 FF FF 7F 1B 80  .....o...K......
00E0: 6F 76 F8 FF FF 7F 00                              ov.....         
```

#### Opcodes

```
  0: 0x00C8 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00CB [0x1F] MOVE_ENTITY: EventEntity moves to X=61.217*, Z=-216.506*, Y=-23.915*
  2: 0x00D3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00D5 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00D6 [0x1C] WAIT(10* ticks)
  5: 0x00D9 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=9.3°*)
  6: 0x00E0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x00E1 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  8: 0x00E6 [0x00] END_REQSTACK()
```
