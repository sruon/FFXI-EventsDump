# 17105582 - Vestillet

## Common Data

| Field            | Value                            |
|------------------|----------------------------------|
| Zone             | Southern San d'Oria [S] (ID: 80) |
| Block Size       | 628 bytes                        |
| Total Events     | 26                               |
| References Count | 33                               |

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
| [65535.7](#event-655357)   | 0x003A       |     11 |              3 |
| [86](#event-86)            | 0x0045       |      1 |              1 |
| [65535.8](#event-655358)   | 0x0046       |     35 |              9 |
| [89](#event-89)            | 0x0069       |      1 |              1 |
| [65535.9](#event-655359)   | 0x006A       |     13 |              3 |
| [65535.10](#event-6553510) | 0x0077       |     13 |              3 |
| [65535.11](#event-6553511) | 0x0084       |     25 |              3 |
| [151](#event-151)          | 0x009D       |      1 |              1 |
| [154](#event-154)          | 0x009E       |      1 |              1 |
| [65535.12](#event-6553512) | 0x009F       |     21 |              2 |
| [147](#event-147)          | 0x00B4       |      7 |              2 |
| [65535.13](#event-6553513) | 0x00BB       |     22 |              6 |
| [148](#event-148)          | 0x00D1       |      1 |              1 |
| [169](#event-169)          | 0x00D2       |      1 |              1 |
| [65535.14](#event-6553514) | 0x00D3       |     19 |              5 |
| [65535.15](#event-6553515) | 0x00E6       |     20 |              5 |
| [65535.16](#event-6553516) | 0x00FA       |     29 |              6 |
| [65535.17](#event-6553517) | 0x0117       |     75 |             16 |
| [65535.18](#event-6553518) | 0x0162       |     21 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0000      |           0 |
|       1 | 0x0001      |           1 |
|       2 | 0x0080      |         128 |
|       3 | 0x000D      |          13 |
|       4 | 0x0002      |           2 |
|       5 | 0x002B      |          43 |
|       6 | 0x0003      |           3 |
|       7 | 0x00D9      |         217 |
|       8 | 0x000C      |          12 |
|       9 | 0x00DD      |         221 |
|      10 | 0x00FA      |         250 |
|      11 | 0x001B      |          27 |
|      12 | 0xFFFFA6D7  |  4294944471 |
|      13 | 0xFFFFF192  |  4294963602 |
|      14 | 0x001E      |          30 |
|      15 | 0x03E8      |        1000 |
|      16 | 0xA788      |       42888 |
|      17 | 0xFFFFF830  |  4294965296 |
|      18 | 0x156B4     |       87732 |
|      19 | 0x1C4EE     |      115950 |
|      20 | 0x18486     |       99462 |
|      21 | 0x195BF     |      103871 |
|      22 | 0x03E7      |         999 |
|      23 | 0x0A28      |        2600 |
|      24 | 0x15F0A     |       89866 |
|      25 | 0x1BD03     |      113923 |
|      26 | 0x1585E     |       88158 |
|      27 | 0x1D154     |      119124 |
|      28 | 0x15CE0     |       89312 |
|      29 | 0x1D40C     |      119820 |
|      30 | 0x163E2     |       91106 |
|      31 | 0x1D6B2     |      120498 |
|      32 | 0x0696      |        1686 |

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
| Data Size    | 11 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                6C F8 FF FF 7F 02            l.....
0040: 80 01 80 00 00                                    .....           
```

#### Opcodes

```
  0: 0x003A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=128*, fade_time=1*)
  1: 0x0043 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0044 [0x00] END_REQSTACK()
```

### Event 86

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0045  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                00                                      .          
```

#### Opcodes

```
  0: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   03 00  00 25 10 03 02 00 27 10        ...%....'.
0050: 03 01 00 26 10 03 03 00  28 10 32 03 80 1F 00 00  ...&....(.2.....
0060: 00 02 00 01 00 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x0046 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[37]
  1: 0x004B [0x03] ExtData[1]->WorkLocal[2] = Work_Zone[39]
  2: 0x0050 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[38]
  3: 0x0055 [0x03] ExtData[1]->WorkLocal[3] = Work_Zone[40]
  4: 0x005A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  5: 0x005D [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[0], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[1]
  6: 0x0065 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0067 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0068 [0x00] END_REQSTACK()
```

### Event 89

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0069  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             00                             .      
```

#### Opcodes

```
  0: 0x0069 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006A   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                6E F8 FF FF 7F 04            n.....
0070: 80 99 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x006A [0x6E] EventEntity uses emote 2*
  1: 0x0071 [0x99] Wait for EventEntity animation to complete
  2: 0x0076 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0077   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                      6E  F8 FF FF 7F 05 80 99 F8         n........
0080: FF FF 7F 00                                       ....            
```

#### Opcodes

```
  0: 0x0077 [0x6E] EventEntity uses emote 43*
  1: 0x007E [0x99] Wait for EventEntity animation to complete
  2: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 25 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             7E 06 AE 02  05 01 01 80 00 80 01 80      ~...........
0090: 01 80 01 80 01 80 7E 04  AE 02 05 01 00           ......~......   
```

#### Opcodes

```
  0: 0x0084 [0x7E] CHOCOBO_MOUNT: Mode 6 (custom mount) on Vestillet (ID: 17105582/0x010502AE)
  1: 0x0096 [0x7E] CHOCOBO_MOUNT: Mode 4 on Vestillet (ID: 17105582/0x010502AE)
  2: 0x009C [0x00] END_REQSTACK()
```

### Event 151

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         00                     .  
```

#### Opcodes

```
  0: 0x009D [0x00] END_REQSTACK()
```

### Event 154

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                            00                   . 
```

#### Opcodes

```
  0: 0x009E [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009F   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                               B6                 .
00A0: 0B 06 80 04 80 00 80 07  80 03 80 08 80 09 80 0A  ................
00B0: 80 0B 80 00                                       ....            
```

#### Opcodes

```
  0: 0x009F [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=2*, head=0*, body=217*, hands=13*, legs=12*, feet=221*, main=250*, sub=27*)
  1: 0x00B3 [0x00] END_REQSTACK()
```

### Event 147

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B4  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             92 01 F8 FF  FF 7F 00                     .......     
```

#### Opcodes

```
  0: 0x00B4 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00BA [0x00] END_REQSTACK()
```

### Event 65535.13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BB   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                   32 03 80 1F 00             2....
00C0: 0C 80 0D 80 00 80 1F 01  1E 86 02 05 01 1C 0E 80  ................
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00BB [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00BE [0x1F] MOVE_ENTITY: EventEntity moves to X=-22.825*, Z=-3.694*, Y=0.000*
  2: 0x00C6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00C8 [0x1E] EventEntity looks at Ragelise (ID: 17105542/0x01050286) and starts talking
  4: 0x00CD [0x1C] WAIT(30* ticks)
  5: 0x00D0 [0x00] END_REQSTACK()
```

### Event 148

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D1  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    00                                              .              
```

#### Opcodes

```
  0: 0x00D1 [0x00] END_REQSTACK()
```

### Event 169

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D2  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:       00                                            .             
```

#### Opcodes

```
  0: 0x00D2 [0x00] END_REQSTACK()
```

### Event 65535.14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D3   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:          32 03 80 1F 00  0F 80 10 80 11 80 1F 01     2............
00E0: 1E EF 01 05 01 00                                 ......          
```

#### Opcodes

```
  0: 0x00D3 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00D6 [0x1F] MOVE_ENTITY: EventEntity moves to X=1.000*, Z=42.888*, Y=-2.000*
  2: 0x00DE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00E0 [0x1E] EventEntity looks at Raustigne (ID: 17105391/0x010501EF) and starts talking
  4: 0x00E5 [0x00] END_REQSTACK()
```

### Event 65535.15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00E6   |
| Data Size    | 20 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                   59 04  F8 FF FF 7F 03 80 1F 00        Y.........
00F0: 12 80 13 80 0F 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x00E6 [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x00EE [0x1F] MOVE_ENTITY: EventEntity moves to X=87.732*, Z=115.950*, Y=1.000*
  2: 0x00F6 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00F8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00F9 [0x00] END_REQSTACK()
```

### Event 65535.16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FA   |
| Data Size    | 29 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                59 04 F8 FF FF 7F            Y.....
0100: 03 80 1F 00 14 80 15 80  16 80 1F 01 6F 4A F8 FF  ............oJ..
0110: FF 7F 8B 02 05 01 00                              .......         
```

#### Opcodes

```
  0: 0x00FA [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  1: 0x0102 [0x1F] MOVE_ENTITY: EventEntity moves to X=99.462*, Z=103.871*, Y=0.999*
  2: 0x010A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x010C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x010D [0x4A] EventEntity looks at Mayakov (ID: 17105547/0x0105028B)
  5: 0x0116 [0x00] END_REQSTACK()
```

### Event 65535.17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0117   |
| Data Size    | 75 bytes |
| Instructions | 16       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                      7B  F8 FF FF 7F 59 04 F8 FF         {....Y...
0120: FF 7F 03 80 4B F8 FF FF  7F 17 80 6F 76 F8 FF FF  ....K......ov...
0130: 7F 1F 00 18 80 19 80 00  80 1F 01 1F 00 1A 80 1B  ................
0140: 80 0F 80 1F 01 1F 00 1C  80 1D 80 0F 80 1F 01 1F  ................
0150: 00 1E 80 1F 80 0F 80 1F  01 6F 4B F8 FF FF 7F 20  .........oK.... 
0160: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0117 [0x7B] EventEntity stops talking
  1: 0x011C [0x59] UPDATE_ENTITY_DATA: Set EventEntity main speed = 13* * 0.1
  2: 0x0124 [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=14.3°*)
  3: 0x012B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x012C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  5: 0x0131 [0x1F] MOVE_ENTITY: EventEntity moves to X=89.866*, Z=113.923*, Y=0.000*
  6: 0x0139 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x013B [0x1F] MOVE_ENTITY: EventEntity moves to X=88.158*, Z=119.124*, Y=1.000*
  8: 0x0143 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0145 [0x1F] MOVE_ENTITY: EventEntity moves to X=89.312*, Z=119.820*, Y=1.000*
 10: 0x014D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x014F [0x1F] MOVE_ENTITY: EventEntity moves to X=91.106*, Z=120.498*, Y=1.000*
 12: 0x0157 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 13: 0x0159 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 14: 0x015A [0x4B] UPDATE_ENTITY_YAW(entity=EventEntity, yaw=9.3°*)
 15: 0x0161 [0x00] END_REQSTACK()
```

### Event 65535.18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0162   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:       B6 0B 06 80 04 80  00 80 07 80 03 80 08 80    ..............
0170: 09 80 00 80 00 80 00                              .......         
```

#### Opcodes

```
  0: 0x0162 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=2*, head=0*, body=217*, hands=13*, legs=12*, feet=221*, main=0*, sub=0*)
  1: 0x0176 [0x00] END_REQSTACK()
```
