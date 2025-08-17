# 16908437 - Shikaree Z

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Sealion's Den (ID: 32) |
| Block Size       | 668 bytes              |
| Total Events     | 19                     |
| References Count | 52                     |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |     13 |              3 |
| [33](#event-33)            | 0x000D       |     10 |              2 |
| [65535.1](#event-655351)   | 0x0017       |     29 |              6 |
| [1](#event-1)              | 0x0034       |     10 |              2 |
| [2](#event-2)              | 0x003E       |     10 |              2 |
| [65535.2](#event-655352)   | 0x0048       |     14 |              4 |
| [65535.3](#event-655353)   | 0x0056       |     27 |              4 |
| [65535.4](#event-655354)   | 0x0071       |     72 |             11 |
| [31](#event-31)            | 0x00B9       |      7 |              2 |
| [32](#event-32)            | 0x00C0       |      7 |              2 |
| [65535.5](#event-655355)   | 0x00C7       |     10 |              2 |
| [65535.6](#event-655356)   | 0x00D1       |     10 |              2 |
| [65535.7](#event-655357)   | 0x00DB       |     32 |              6 |
| [65535.8](#event-655358)   | 0x00FB       |     16 |              5 |
| [15](#event-15)            | 0x010B       |     10 |              2 |
| [65535.9](#event-655359)   | 0x0115       |     21 |              5 |
| [65535.10](#event-6553510) | 0x012A       |     16 |              2 |
| [65535.11](#event-6553511) | 0x013A       |     29 |              3 |
| [65535.12](#event-6553512) | 0x0157       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFF6145E  |  4294317150 |
|       1 | 0x7E92D     |      518445 |
|       2 | 0xFFFC7914  |  4294736148 |
|       3 | 0x0D82      |        3458 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFF64536  |  4294329654 |
|       6 | 0x80C24     |      527396 |
|       7 | 0xFFFC784D  |  4294735949 |
|       8 | 0xFFF63846  |  4294326342 |
|       9 | 0x80DDD     |      527837 |
|      10 | 0x04FA      |        1274 |
|      11 | 0xFFF41792  |  4294186898 |
|      12 | 0xFFFEB3DA  |  4294882266 |
|      13 | 0xFFFE6C4D  |  4294863949 |
|      14 | 0x0C1A      |        3098 |
|      15 | 0x000D      |          13 |
|      16 | 0xFFF41920  |  4294187296 |
|      17 | 0xFFFEBCB8  |  4294884536 |
|      18 | 0xFFF5B409  |  4294292489 |
|      19 | 0x7DFC6     |      516038 |
|      20 | 0xFFFC7944  |  4294736196 |
|      21 | 0x0F0E      |        3854 |
|      22 | 0x0299      |         665 |
|      23 | 0x0001      |           1 |
|      24 | 0x218E      |        8590 |
|      25 | 0x1F15      |        7957 |
|      26 | 0xFFFC79A8  |  4294736296 |
|      27 | 0xFFFFFE00  |  4294966784 |
|      28 | 0xFFF66020  |  4294336544 |
|      29 | 0xFFF667C4  |  4294338500 |
|      30 | 0x303CA     |      197578 |
|      31 | 0x0EBF      |        3775 |
|      32 | 0xFFF40A37  |  4294183479 |
|      33 | 0xFFFED367  |  4294890343 |
|      34 | 0xFFFE6D14  |  4294864148 |
|      35 | 0x0CA9      |        3241 |
|      36 | 0xFFF42EF1  |  4294192881 |
|      37 | 0xFFFEEDD0  |  4294897104 |
|      38 | 0x0CFB      |        3323 |
|      39 | 0xFFF417DE  |  4294186974 |
|      40 | 0xFFFEA52C  |  4294878508 |
|      41 | 0x961E9     |      614889 |
|      42 | 0xBD592     |      775570 |
|      43 | 0x20658     |      132696 |
|      44 | 0x0753      |        1875 |
|      45 | 0x00CF      |         207 |
|      46 | 0x9576D     |      612205 |
|      47 | 0xBB920     |      768288 |
|      48 | 0x20645     |      132677 |
|      49 | 0x93E2C     |      605740 |
|      50 | 0xB98AD     |      759981 |
|      51 | 0x20C91     |      134289 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 92 01 F8 FF FF 7F 94 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0006 [0x94] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 00 80               7..
0010: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-650.146*, z=518.445*, y=-231.148*, direction=303.9°*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 29 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      79  00 F8 FF FF 7F F0 FF FF         y........
0020: 7F 32 04 80 1F 00 05 80  06 80 07 80 1F 01 1E A0  .2..............
0030: 00 02 01 00                                       ....            
```

#### Opcodes

```
  0: 0x0017 [0x79] EventEntity looks at LocalPlayer (Basic look)
  1: 0x0021 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=-637.642*, Z=527.396*, Y=-231.347*
  3: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x002E [0x1E] EventEntity looks at Nag'molada (ID: 16908448/0x010200A0) and starts talking
  5: 0x0033 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             37 08 80 09  80 07 80 0A 80 00            7.........  
```

#### Opcodes

```
  0: 0x0034 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-640.954*, z=527.837*, y=-231.347*, direction=112.0°*
  1: 0x003D [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003E   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                            37 0B                7.
0040: 80 0C 80 0D 80 0E 80 00                           ........        
```

#### Opcodes

```
  0: 0x003E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-780.398*, z=-85.030*, y=-103.347*, direction=272.3°*
  1: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0048   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          32 0F 80 1F 00 10 80 11          2.......
0050: 80 0D 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0048 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=-780.000*, Z=-82.760*, Y=-103.347*
  2: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 27 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   33 01  37 12 80 13 80 14 80 15        3.7.......
0060: 80 5B 16 80 F8 FF FF 7F  F8 FF FF 7F 61 74 73 30  .[..........ats0
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x0056 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0058 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-674.807*, z=516.038*, y=-231.100*, direction=338.7°*
  2: 0x0061 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ats0" with entities [EventEntity, EventEntity], work=665*
  3: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 72 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    33 01 79 00 F8 FF FF  7F 90 00 02 01 5B 16 80   3.y.........[..
0080: F8 FF FF 7F F8 FF FF 7F  61 74 73 30 02 24 10 17  ........ats0.$..
0090: 80 01 B8 00 3B 9F 00 02  01 00 00 01 00 02 00 07  ....;...........
00A0: 00 00 18 80 07 01 00 19  80 37 00 00 01 00 1A 80  .........7......
00B0: 1B 80 1C 17 80 01 8C 00  00                       .........       
```

#### Opcodes

```
  0: 0x0071 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0073 [0x79] EventEntity looks at Tenzen (ID: 16908432/0x01020090) (Basic look)
  2: 0x007D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ats0" with entities [EventEntity, EventEntity], work=665*
  3: 0x008C [0x02] IF !(Work_Zone[36] == 1*) GOTO 0x00B8
  4: 0x0094 [0x3B] GET_ENTITY_POSITION(entity=ship (ID: 16908447/0x0102009F), x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[1], z_destination=ExtData[1]->WorkLocal[2])
  5: 0x009F [0x07] ExtData[1]->WorkLocal[0] += 8590*
  6: 0x00A4 [0x07] ExtData[1]->WorkLocal[1] += 7957*
  7: 0x00A9 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=ExtData[1]->WorkLocal[0], z=ExtData[1]->WorkLocal[1], y=-231.000*, direction=377476174.2°*
  8: 0x00B2 [0x1C] WAIT(1* ticks)
  9: 0x00B5 [0x01] GOTO 0x008C
 10: 0x00B8 [0x00] END_REQSTACK()
```

### Event 31

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B9  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             94 01 F8 FF FF 7F 00           .......
```

#### Opcodes

```
  0: 0x00B9 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00BF [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C0  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0: 94 01 F8 FF FF 7F 00                              .......         
```

#### Opcodes

```
  0: 0x00C0 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x00C6 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C7   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                      37  1C 80 1D 80 1E 80 1F 80         7........
00D0: 00                                                .               
```

#### Opcodes

```
  0: 0x00C7 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-630.752*, z=-628.796*, y=197.578*, direction=331.8°*
  1: 0x00D0 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D1   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:    37 20 80 21 80 22 80  23 80 00                  7 .!.".#..     
```

#### Opcodes

```
  0: 0x00D1 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-783.817*, z=-76.953*, y=-103.148*, direction=284.8°*
  1: 0x00DA [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00DB   |
| Data Size    | 32 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                   37 24 80 25 80             7$.%.
00E0: 22 80 26 80 1E 8D 00 02  01 6F 70 5B 16 80 F8 FF  ".&......op[....
00F0: FF 7F F8 FF FF 7F 61 74  73 30 00                 ......ats0.     
```

#### Opcodes

```
  0: 0x00DB [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-774.415*, z=-70.192*, y=-103.148*, direction=292.1°*
  1: 0x00E4 [0x1E] EventEntity looks at Prishe (ID: 16908429/0x0102008D) and starts talking
  2: 0x00E9 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00EA [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00EB [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ats0" with entities [EventEntity, EventEntity], work=665*
  5: 0x00FA [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00FB   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:                                   32 04 80 1F 00             2....
0100: 27 80 28 80 0D 80 1F 01  22 01 00                 '.(....."..     
```

#### Opcodes

```
  0: 0x00FB [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x00FE [0x1F] MOVE_ENTITY: EventEntity moves to X=-780.322*, Z=-88.788*, Y=-103.347*
  2: 0x0106 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0108 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x010A [0x00] END_REQSTACK()
```

### Event 15

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x010B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:                                   37 29 80 2A 80             7).*.
0110: 2B 80 2C 80 00                                    +.,..           
```

#### Opcodes

```
  0: 0x010B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=614.889*, z=775.570*, y=132.696*, direction=164.8°*
  1: 0x0114 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0115   |
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                39 2D 80  6F 70 5B 16 80 F8 FF FF       9-.op[.....
0120: 7F F8 FF FF 7F 61 74 73  30 00                    .....ats0.      
```

#### Opcodes

```
  0: 0x0115 [0x39] SET_ENTITY_DIRECTION(direction=1.1°*)
  1: 0x0118 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0119 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x011A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ats0" with entities [EventEntity, EventEntity], work=665*
  4: 0x0129 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x012A   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120:                                5B 16 80 F8 FF FF            [.....
0130: 7F F8 FF FF 7F 61 74 73  30 00                    .....ats0.      
```

#### Opcodes

```
  0: 0x012A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ats0" with entities [EventEntity, EventEntity], work=665*
  1: 0x0139 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x013A   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                5B 16 80 F8 FF FF            [.....
0140: 7F F8 FF FF 7F 61 74 65  30 53 F8 FF FF 7F F8 FF  .....ate0S......
0150: FF 7F 61 74 65 30 00                              ..ate0.         
```

#### Opcodes

```
  0: 0x013A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ate0" with entities [EventEntity, EventEntity], work=665*
  1: 0x0149 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "ate0" with entities [EventEntity, EventEntity]
  2: 0x0156 [0x00] END_REQSTACK()
```

### Event 65535.12

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0157   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                      32  0F 80 1F 00 2E 80 2F 80         2....../.
0160: 30 80 1F 01 1F 00 31 80  32 80 33 80 1F 01 00     0.....1.2.3.... 
```

#### Opcodes

```
  0: 0x0157 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x015A [0x1F] MOVE_ENTITY: EventEntity moves to X=612.205*, Z=768.288*, Y=132.677*
  2: 0x0162 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0164 [0x1F] MOVE_ENTITY: EventEntity moves to X=605.740*, Z=759.981*, Y=134.289*
  4: 0x016C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x016E [0x00] END_REQSTACK()
```
