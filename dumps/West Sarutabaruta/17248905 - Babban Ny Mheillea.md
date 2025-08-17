# 17248905 - Babban Ny Mheillea

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | West Sarutabaruta (ID: 115) |
| Block Size       | 752 bytes                   |
| Total Events     | 13                          |
| References Count | 52                          |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [80](#event-80)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |    198 |             25 |
| [65535.2](#event-655352)   | 0x00C8       |     58 |              8 |
| [65535.3](#event-655353)   | 0x0102       |     51 |              7 |
| [65535.4](#event-655354)   | 0x0135       |      1 |              1 |
| [65535.5](#event-655355)   | 0x0136       |     23 |              5 |
| [65535.6](#event-655356)   | 0x014D       |     28 |              8 |
| [65535.7](#event-655357)   | 0x0169       |     47 |             11 |
| [65535.8](#event-655358)   | 0x0198       |     10 |              2 |
| [65535.9](#event-655359)   | 0x01A2       |     14 |              4 |
| [65535.10](#event-6553510) | 0x01B0       |     24 |              6 |
| [65535.11](#event-6553511) | 0x01C8       |     17 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x0061      |          97 |
|       2 | 0x000C      |          12 |
|       3 | 0x0004      |           4 |
|       4 | 0x000F      |          15 |
|       5 | 0xB008F     |      721039 |
|       6 | 0x91901     |      596225 |
|       7 | 0xFFFFC174  |  4294951284 |
|       8 | 0x09F2      |        2546 |
|       9 | 0xAFAB7     |      719543 |
|      10 | 0x90EDA     |      593626 |
|      11 | 0xFFFFC1BE  |  4294951358 |
|      12 | 0xB0D8C     |      724364 |
|      13 | 0x90639     |      591417 |
|      14 | 0xFFFFC1FC  |  4294951420 |
|      15 | 0xB0562     |      722274 |
|      16 | 0x91902     |      596226 |
|      17 | 0xFFFFC181  |  4294951297 |
|      18 | 0xB02EE     |      721646 |
|      19 | 0x8FB52     |      588626 |
|      20 | 0xFFFFC2EF  |  4294951663 |
|      21 | 0x004B      |          75 |
|      22 | 0xA5702     |      677634 |
|      23 | 0x8FD1A     |      589082 |
|      24 | 0xFFFF5FD8  |  4294926296 |
|      25 | 0x0871      |        2161 |
|      26 | 0xFFFF600A  |  4294926346 |
|      27 | 0x09EC      |        2540 |
|      28 | 0x76AC      |       30380 |
|      29 | 0xFFFFFC18  |  4294966296 |
|      30 | 0x01CC      |         460 |
|      31 | 0x0019      |          25 |
|      32 | 0x2472      |        9330 |
|      33 | 0x4F87      |       20359 |
|      34 | 0x0018      |          24 |
|      35 | 0x0A44      |        2628 |
|      36 | 0x7705      |       30469 |
|      37 | 0x000A      |          10 |
|      38 | 0x24CB      |        9419 |
|      39 | 0x4F12      |       20242 |
|      40 | 0x001E      |          30 |
|      41 | 0x0096      |         150 |
|      42 | 0x101E      |        4126 |
|      43 | 0x6CA6      |       27814 |
|      44 | 0x0ADC      |        2780 |
|      45 | 0xFFFFF349  |  4294964041 |
|      46 | 0xAD02      |       44290 |
|      47 | 0x0027      |          39 |
|      48 | 0x1114D     |       69965 |
|      49 | 0x31ADD     |      203485 |
|      50 | 0xFFFFFCF9  |  4294966521 |
|      51 | 0x0015      |          21 |

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

### Event 80

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

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 198 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1C 00 80 35 01 80  77 02 80 03 80 1C 04 80    ...5..w.......
0010: 29 10 8E 32 07 01 03 2F  00 8E 32 07 01 4E 00 8E  )..2.../..2..N..
0020: 32 07 01 94 01 8E 32 07  01 BA 89 32 07 01 05 80  2.....2....2....
0030: 06 80 07 80 08 80 BA 8B  32 07 01 09 80 0A 80 0B  ........2.......
0040: 80 08 80 BA 8C 32 07 01  0C 80 0D 80 0E 80 08 80  .....2..........
0050: BA 8D 32 07 01 0F 80 10  80 11 80 08 80 BA 8E 32  ..2............2
0060: 07 01 12 80 13 80 14 80  08 80 80 89 32 07 01 80  ............2...
0070: 8B 32 07 01 80 8C 32 07  01 80 8D 32 07 01 80 8E  .2....2....2....
0080: 32 07 01 1C 15 80 2C 89  32 07 01 89 32 07 01 63  2.....,.2...2..c
0090: 6F 72 70 2C 8B 32 07 01  8B 32 07 01 63 6F 72 70  orp,.2...2..corp
00A0: 2C 8C 32 07 01 8C 32 07  01 63 6F 72 70 2C 8D 32  ,.2...2..corp,.2
00B0: 07 01 8D 32 07 01 63 6F  72 70 2C 8E 32 07 01 8E  ...2..corp,.2...
00C0: 32 07 01 63 6F 72 70 00                           2..corp.        
```

#### Opcodes

```
  0: 0x0002 [0x1C] WAIT(60* ticks)
  1: 0x0005 [0x35] LOAD_ZONE_NO_CLOSE(zone_id=97*)
  2: 0x0008 [0x77] SET_EVENT_TIME_WEATHER(hour=12*, weather=4*)
  3: 0x000D [0x1C] WAIT(15* ticks)
  4: 0x0010 [0x29] REQ_SET_WAIT(priority=0x10, entity_id=Darach (ID: 17248910/0x0107328E), tag_num=0x03)
  5: 0x0017 [0x2F] Darach (ID: 17248910/0x0107328E)->Render.Flags0 &= ~0x80000 // Bit 19
  6: 0x001D [0x4E] SET_ENTITY_HIDE_FLAG: Show Darach (ID: 17248910/0x0107328E)
  7: 0x0023 [0x94] Darach (ID: 17248910/0x0107328E)->Render.Flags3 ^= 0x01
  8: 0x0029 [0xBA] SET_ENTITY_POSITION(entity_id=Babban Ny Mheillea (ID: 17248905/0x01073289), pos_x=721.039*, pos_z=596.225*, pos_y=-16.012*, direction=223.8°*)
  9: 0x0036 [0xBA] SET_ENTITY_POSITION(entity_id=Abenzio (ID: 17248907/0x0107328B), pos_x=719.543*, pos_z=593.626*, pos_y=-15.938*, direction=223.8°*)
 10: 0x0043 [0xBA] SET_ENTITY_POSITION(entity_id=Bryher (ID: 17248908/0x0107328C), pos_x=724.364*, pos_z=591.417*, pos_y=-15.876*, direction=223.8°*)
 11: 0x0050 [0xBA] SET_ENTITY_POSITION(entity_id=Camlin (ID: 17248909/0x0107328D), pos_x=722.274*, pos_z=596.226*, pos_y=-15.999*, direction=223.8°*)
 12: 0x005D [0xBA] SET_ENTITY_POSITION(entity_id=Darach (ID: 17248910/0x0107328E), pos_x=721.646*, pos_z=588.626*, pos_y=-15.633*, direction=223.8°*)
 13: 0x006A [0x80] LOAD_WAIT(entity=Babban Ny Mheillea (ID: 17248905/0x01073289))
 14: 0x006F [0x80] LOAD_WAIT(entity=Abenzio (ID: 17248907/0x0107328B))
 15: 0x0074 [0x80] LOAD_WAIT(entity=Bryher (ID: 17248908/0x0107328C))
 16: 0x0079 [0x80] LOAD_WAIT(entity=Camlin (ID: 17248909/0x0107328D))
 17: 0x007E [0x80] LOAD_WAIT(entity=Darach (ID: 17248910/0x0107328E))
 18: 0x0083 [0x1C] WAIT(75* ticks)
 19: 0x0086 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "corp" with entities [Babban Ny Mheillea (ID: 17248905/0x01073289), Babban Ny Mheillea (ID: 17248905/0x01073289)]
 20: 0x0093 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "corp" with entities [Abenzio (ID: 17248907/0x0107328B), Abenzio (ID: 17248907/0x0107328B)]
 21: 0x00A0 [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "corp" with entities [Bryher (ID: 17248908/0x0107328C), Bryher (ID: 17248908/0x0107328C)]
 22: 0x00AD [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "corp" with entities [Camlin (ID: 17248909/0x0107328D), Camlin (ID: 17248909/0x0107328D)]
 23: 0x00BA [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "corp" with entities [Darach (ID: 17248910/0x0107328E), Darach (ID: 17248910/0x0107328E)]
 24: 0x00C7 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C8   |
| Data Size    | 58 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                          2F 00 89 32 07 01 4E 00          /..2..N.
00D0: 89 32 07 01 94 01 89 32  07 01 92 01 89 32 07 01  .2.....2.....2..
00E0: BA 89 32 07 01 16 80 17  80 18 80 08 80 80 89 32  ..2............2
00F0: 07 01 5B 19 80 89 32 07  01 89 32 07 01 73 6B 79  ..[...2...2..sky
0100: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x00C8 [0x2F] Babban Ny Mheillea (ID: 17248905/0x01073289)->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x00CE [0x4E] SET_ENTITY_HIDE_FLAG: Show Babban Ny Mheillea (ID: 17248905/0x01073289)
  2: 0x00D4 [0x94] Babban Ny Mheillea (ID: 17248905/0x01073289)->Render.Flags3 ^= 0x01
  3: 0x00DA [0x92] Babban Ny Mheillea (ID: 17248905/0x01073289)->Render.Flags3 ^= 0x01
  4: 0x00E0 [0xBA] SET_ENTITY_POSITION(entity_id=Babban Ny Mheillea (ID: 17248905/0x01073289), pos_x=677.634*, pos_z=589.082*, pos_y=-41.000*, direction=223.8°*)
  5: 0x00ED [0x80] LOAD_WAIT(entity=Babban Ny Mheillea (ID: 17248905/0x01073289))
  6: 0x00F2 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "sky0" with entities [Babban Ny Mheillea (ID: 17248905/0x01073289), Babban Ny Mheillea (ID: 17248905/0x01073289)], work=2161*
  7: 0x0101 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0102   |
| Data Size    | 51 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0100:       2F 00 89 32 07 01  4E 00 89 32 07 01 6B 69    /..2..N..2..ki
0110: 64 6C 30 89 32 07 01 94  01 89 32 07 01 92 01 89  dl0.2.....2.....
0120: 32 07 01 BA 89 32 07 01  16 80 17 80 1A 80 08 80  2....2..........
0130: 80 89 32 07 01                                    ..2..           
```

#### Opcodes

```
  0: 0x0102 [0x2F] Babban Ny Mheillea (ID: 17248905/0x01073289)->Render.Flags0 &= ~0x80000 // Bit 19
  1: 0x0108 [0x4E] SET_ENTITY_HIDE_FLAG: Show Babban Ny Mheillea (ID: 17248905/0x01073289)
  2: 0x010E [0x6B] STOP_AND_IDLE: Babban Ny Mheillea (ID: 17248905/0x01073289) stops current action and resets to idle (animation="idl0")
  3: 0x0117 [0x94] Babban Ny Mheillea (ID: 17248905/0x01073289)->Render.Flags3 ^= 0x01
  4: 0x011D [0x92] Babban Ny Mheillea (ID: 17248905/0x01073289)->Render.Flags3 ^= 0x01
  5: 0x0123 [0xBA] SET_ENTITY_POSITION(entity_id=Babban Ny Mheillea (ID: 17248905/0x01073289), pos_x=677.634*, pos_z=589.082*, pos_y=-40.950*, direction=223.8°*)
  6: 0x0130 [0x80] LOAD_WAIT(entity=Babban Ny Mheillea (ID: 17248905/0x01073289))
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0135  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                00                                      .          
```

#### Opcodes

```
  0: 0x0135 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0136   |
| Data Size    | 23 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                   37 1B  80 1C 80 1D 80 1E 80 32        7........2
0140: 1F 80 1F 00 20 80 21 80  1D 80 1F 01 00           .... .!......   
```

#### Opcodes

```
  0: 0x0136 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=2.540*, z=30.380*, y=-1.000*, direction=40.4°*
  1: 0x013F [0x32] ExtData[1]->MainSpeed = 25* * 0.1
  2: 0x0142 [0x1F] MOVE_ENTITY: EventEntity moves to X=9.330*, Z=20.359*, Y=-1.000*
  3: 0x014A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x014C [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014D   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                         4A 89 32               J.2
0150: 07 01 8B 32 07 01 6F 70  1C 00 80 32 22 80 1F 00  ...2..op...2"...
0160: 23 80 24 80 1D 80 1F 01  00                       #.$......       
```

#### Opcodes

```
  0: 0x014D [0x4A] Babban Ny Mheillea (ID: 17248905/0x01073289) looks at Abenzio (ID: 17248907/0x0107328B)
  1: 0x0156 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0157 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0158 [0x1C] WAIT(60* ticks)
  4: 0x015B [0x32] ExtData[1]->MainSpeed = 24* * 0.1
  5: 0x015E [0x1F] MOVE_ENTITY: EventEntity moves to X=2.628*, Z=30.469*, Y=-1.000*
  6: 0x0166 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0168 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0169   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                             32 25 80 1F 00 26 80           2%...&.
0170: 27 80 1D 80 1F 01 6F 4A  89 32 07 01 F0 FF FF 7F  '.....oJ.2......
0180: 6F 70 1C 28 80 5B 19 80  89 32 07 01 89 32 07 01  op.(.[...2...2..
0190: 74 6C 6B 30 1C 29 80 00                           tlk0.)..        
```

#### Opcodes

```
  0: 0x0169 [0x32] ExtData[1]->MainSpeed = 10* * 0.1
  1: 0x016C [0x1F] MOVE_ENTITY: EventEntity moves to X=9.419*, Z=20.242*, Y=-1.000*
  2: 0x0174 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0176 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0177 [0x4A] Babban Ny Mheillea (ID: 17248905/0x01073289) looks at LocalPlayer
  5: 0x0180 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0181 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0182 [0x1C] WAIT(30* ticks)
  8: 0x0185 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Babban Ny Mheillea (ID: 17248905/0x01073289), Babban Ny Mheillea (ID: 17248905/0x01073289)], work=2161*
  9: 0x0194 [0x1C] WAIT(150* ticks)
 10: 0x0197 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0198   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                          37 2A 80 2B 80 1D 80 2C          7*.+...,
01A0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x0198 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=4.126*, z=27.814*, y=-1.000*, direction=244.3°*
  1: 0x01A1 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01A2   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01A0:       32 04 80 1F 00 2D  80 2E 80 1D 80 1F 01 00    2....-........
```

#### Opcodes

```
  0: 0x01A2 [0x32] ExtData[1]->MainSpeed = 15* * 0.1
  1: 0x01A5 [0x1F] MOVE_ENTITY: EventEntity moves to X=-3.255*, Z=44.290*, Y=-1.000*
  2: 0x01AD [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01AF [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B0   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0: 32 2F 80 1F 00 30 80 31  80 32 80 1F 01 6F 4A F8  2/...0.1.2...oJ.
01C0: FF FF 7F 8B 32 07 01 00                           ....2...        
```

#### Opcodes

```
  0: 0x01B0 [0x32] ExtData[1]->MainSpeed = 39* * 0.1
  1: 0x01B3 [0x1F] MOVE_ENTITY: EventEntity moves to X=69.965*, Z=203.485*, Y=-0.775*
  2: 0x01BB [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01BD [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x01BE [0x4A] EventEntity looks at Abenzio (ID: 17248907/0x0107328B)
  5: 0x01C7 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01C8   |
| Data Size    | 17 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01C0:                          32 33 80 1F 00 1B 80 1C          23......
01D0: 80 1D 80 1F 01 39 1E 80  00                       .....9...       
```

#### Opcodes

```
  0: 0x01C8 [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x01CB [0x1F] MOVE_ENTITY: EventEntity moves to X=2.540*, Z=30.380*, Y=-1.000*
  2: 0x01D3 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x01D5 [0x39] SET_ENTITY_DIRECTION(direction=2.5°*)
  4: 0x01D8 [0x00] END_REQSTACK()
```
