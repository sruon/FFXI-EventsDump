# 17780752 - Domingart

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 488 bytes             |
| Total Events     | 16                    |
| References Count | 35                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      6 |              3 |
| [63](#event-63)            | 0x0006       |     12 |              3 |
| [164](#event-164)          | 0x0012       |      1 |              1 |
| [163](#event-163)          | 0x0013       |     10 |              2 |
| [132](#event-132)          | 0x001D       |      1 |              1 |
| [65535.1](#event-655351)   | 0x001E       |     10 |              2 |
| [65535.2](#event-655352)   | 0x0028       |     19 |              7 |
| [65535.3](#event-655353)   | 0x003B       |     26 |              7 |
| [65535.4](#event-655354)   | 0x0055       |     15 |              5 |
| [65535.5](#event-655355)   | 0x0064       |      4 |              2 |
| [65535.6](#event-655356)   | 0x0068       |     20 |              4 |
| [65535.7](#event-655357)   | 0x007C       |     56 |             13 |
| [65535.8](#event-655358)   | 0x00B4       |     29 |              3 |
| [65535.9](#event-655359)   | 0x00D1       |     29 |              3 |
| [65535.10](#event-6553510) | 0x00EE       |     29 |              3 |
| [65535.11](#event-6553511) | 0x010B       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFEFA63  |  4294900323 |
|       2 | 0xFFFD5A63  |  4294793827 |
|       3 | 0xFFFFE823  |  4294961187 |
|       4 | 0x0529      |        1321 |
|       5 | 0xFFFEF889  |  4294899849 |
|       6 | 0xFFFD55D5  |  4294792661 |
|       7 | 0x09C7      |        2503 |
|       8 | 0xFFFEC8B6  |  4294887606 |
|       9 | 0xFFFD68FC  |  4294797564 |
|      10 | 0xFFFFE82B  |  4294961195 |
|      11 | 0x092E      |        2350 |
|      12 | 0xFFFEBD83  |  4294884739 |
|      13 | 0xFFFD6F8A  |  4294799242 |
|      14 | 0xFFFFE7DF  |  4294961119 |
|      15 | 0x0028      |          40 |
|      16 | 0xFFFEEDFE  |  4294897150 |
|      17 | 0xFFFD523D  |  4294791741 |
|      18 | 0x000A      |          10 |
|      19 | 0xFFFEC8B8  |  4294887608 |
|      20 | 0xFFFD675A  |  4294797146 |
|      21 | 0xFFFFE82C  |  4294961196 |
|      22 | 0xFFFEB70E  |  4294883086 |
|      23 | 0xFFFD76ED  |  4294801133 |
|      24 | 0xFFFFE890  |  4294961296 |
|      25 | 0xFFFEB59D  |  4294882717 |
|      26 | 0xFFFD8281  |  4294804097 |
|      27 | 0xFFFEAFD7  |  4294881239 |
|      28 | 0xFFFD879C  |  4294805404 |
|      29 | 0xFFFE961F  |  4294874655 |
|      30 | 0xFFFD5E67  |  4294794855 |
|      31 | 0x0000      |           0 |
|      32 | 0xFFFE6DB6  |  4294864310 |
|      33 | 0xFFFD47C8  |  4294789064 |
|      34 | 0x004B      |          75 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 6 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 22 01 32 00 80 00                                 ".2...          
```

#### Opcodes

```
  0: 0x0000 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0005 [0x00] END_REQSTACK()
```

### Event 63

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0006   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   37 01  80 02 80 03 80 04 80 33        7........3
0010: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0006 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-66.973*, z=-173.469*, y=-6.109*, direction=116.1°*
  1: 0x000F [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0011 [0x00] END_REQSTACK()
```

### Event 164

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0012  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       00                                            .             
```

#### Opcodes

```
  0: 0x0012 [0x00] END_REQSTACK()
```

### Event 163

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0013   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:          37 05 80 06 80  03 80 07 80 00              7.........   
```

#### Opcodes

```
  0: 0x0013 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-67.447*, z=-174.635*, y=-6.109*, direction=220.0°*
  1: 0x001C [0x00] END_REQSTACK()
```

### Event 132

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                         00                     .  
```

#### Opcodes

```
  0: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            37 08                7.
0020: 80 09 80 0A 80 0B 80 00                           ........        
```

#### Opcodes

```
  0: 0x001E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-79.690*, z=-169.732*, y=-6.101*, direction=206.5°*
  1: 0x0027 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 19 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          1F 00 0C 80 0D 80 0E 80          ........
0030: 1F 01 6F 1E F0 FF FF 7F  6F 70 00                 ..o.....op.     
```

#### Opcodes

```
  0: 0x0028 [0x1F] MOVE_ENTITY: EventEntity moves to X=-82.557*, Z=-168.054*, Y=-6.177*
  1: 0x0030 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0033 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0038 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0039 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x003A [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003B   |
| Data Size    | 26 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                   32 0F 80 1F 00             2....
0040: 10 80 11 80 03 80 1F 01  6F 33 00 4A 10 50 0F 01  ........o3.J.P..
0050: F0 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x003B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x003E [0x1F] MOVE_ENTITY: EventEntity moves to X=-70.146*, Z=-175.555*, Y=-6.109*
  2: 0x0046 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0048 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0049 [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  5: 0x004B [0x4A] Domingart (ID: 17780752/0x010F5010) looks at LocalPlayer
  6: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                33 01 1F  00 01 80 02 80 03 80 1F       3..........
0060: 01 22 01 00                                       ."..            
```

#### Opcodes

```
  0: 0x0055 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0057 [0x1F] MOVE_ENTITY: EventEntity moves to X=-66.973*, Z=-173.469*, Y=-6.109*
  2: 0x005F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0061 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0064  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             1C 12 80 00                               ....        
```

#### Opcodes

```
  0: 0x0064 [0x1C] WAIT(10* ticks)
  1: 0x0067 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0068   |
| Data Size    | 20 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          1F 00 13 80 14 80 15 80          ........
0070: 1F 01 4A 10 50 0F 01 F0  FF FF 7F 00              ..J.P.......    
```

#### Opcodes

```
  0: 0x0068 [0x1F] MOVE_ENTITY: EventEntity moves to X=-79.688*, Z=-170.150*, Y=-6.100*
  1: 0x0070 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0072 [0x4A] Domingart (ID: 17780752/0x010F5010) looks at LocalPlayer
  3: 0x007B [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007C   |
| Data Size    | 56 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      32 0F 80 1F              2...
0080: 00 16 80 17 80 18 80 1F  01 1F 00 19 80 1A 80 18  ................
0090: 80 1F 01 1F 00 1B 80 1C  80 18 80 1F 01 1F 00 1D  ................
00A0: 80 1E 80 1F 80 1F 01 1F  00 20 80 21 80 1F 80 1F  ......... .!....
00B0: 01 22 01 00                                       ."..            
```

#### Opcodes

```
  0: 0x007C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x007F [0x1F] MOVE_ENTITY: EventEntity moves to X=-84.210*, Z=-166.163*, Y=-6.000*
  2: 0x0087 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0089 [0x1F] MOVE_ENTITY: EventEntity moves to X=-84.579*, Z=-163.199*, Y=-6.000*
  4: 0x0091 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0093 [0x1F] MOVE_ENTITY: EventEntity moves to X=-86.057*, Z=-161.892*, Y=-6.000*
  6: 0x009B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x009D [0x1F] MOVE_ENTITY: EventEntity moves to X=-92.641*, Z=-172.441*, Y=0.000*
  8: 0x00A5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x00A7 [0x1F] MOVE_ENTITY: EventEntity moves to X=-102.986*, Z=-178.232*, Y=0.000*
 10: 0x00AF [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x00B1 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 12: 0x00B3 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B4   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:             5B 22 80 F8  FF FF 7F F8 FF FF 7F 74      [".........t
00C0: 68 6B 31 53 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31  hk1S........thk1
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00B4 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=75*
  1: 0x00C3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x00D0 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D1   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    5B 22 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32   [".........thk2
00E0: 53 F8 FF FF 7F F8 FF FF  7F 74 68 6B 32 00        S........thk2.  
```

#### Opcodes

```
  0: 0x00D1 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=75*
  1: 0x00E0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x00ED [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00EE   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00E0:                                            5B 22                ["
00F0: 80 F8 FF FF 7F F8 FF FF  7F 70 61 73 30 53 F8 FF  .........pas0S..
0100: FF 7F F8 FF FF 7F 70 61  73 30 00                 ......pas0.     
```

#### Opcodes

```
  0: 0x00EE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=75*
  1: 0x00FD [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  2: 0x010A [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x010B  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                   00                         .    
```

#### Opcodes

```
  0: 0x010B [0x00] END_REQSTACK()
```
