# 17735721 - Tall Mountain

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Bastok Mines (ID: 234) |
| Block Size       | 524 bytes              |
| Total Events     | 13                     |
| References Count | 31                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32693](#event-32693)    | 0x0001       |     12 |              6 |
| [55](#event-55)          | 0x000D       |     11 |              5 |
| [85](#event-85)          | 0x0018       |     16 |              8 |
| [176](#event-176)        | 0x0028       |     15 |              3 |
| [180](#event-180)        | 0x0037       |      1 |              1 |
| [65535.1](#event-655351) | 0x0038       |     29 |              7 |
| [65535.2](#event-655352) | 0x0055       |     14 |              4 |
| [182](#event-182)        | 0x0063       |      1 |              1 |
| [65535.3](#event-655353) | 0x0064       |     25 |              6 |
| [591](#event-591)        | 0x007D       |      1 |              1 |
| [593](#event-593)        | 0x007E       |      1 |              1 |
| [598](#event-598)        | 0x007F       |    205 |             30 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x3D04      |       15620 |
|       1 | 0x29ED      |       10733 |
|       2 | 0x29EE      |       10734 |
|       3 | 0x292B      |       10539 |
|       4 | 0xFFFDB472  |  4294816882 |
|       5 | 0xFFFF5C4A  |  4294925386 |
|       6 | 0x0000      |           0 |
|       7 | 0x0A09      |        2569 |
|       8 | 0x000D      |          13 |
|       9 | 0xFFFFBEAB  |  4294950571 |
|      10 | 0x7D0B      |       32011 |
|      11 | 0x1B57      |        6999 |
|      12 | 0x0672      |        1650 |
|      13 | 0xFFFFB4DF  |  4294948063 |
|      14 | 0x7997      |       31127 |
|      15 | 0x11733     |       71475 |
|      16 | 0xFFFFC8C0  |  4294953152 |
|      17 | 0x111AE     |       70062 |
|      18 | 0xFFFFDBBE  |  4294958014 |
|      19 | 0x0E89      |        3721 |
|      20 | 0x0002      |           2 |
|      21 | 0x11429     |       70697 |
|      22 | 0xFFFFC1BE  |  4294951358 |
|      23 | 0x0C8A      |        3210 |
|      24 | 0x0066      |         102 |
|      25 | 0x00F0      |         240 |
|      26 | 0x28E2      |       10466 |
|      27 | 0x00C8      |         200 |
|      28 | 0x0078      |         120 |
|      29 | 0x09BF      |        2495 |
|      30 | 0x0C2F      |        3119 |

## String References

- **10466**: I don't know how you got inside, but that area is off limits. Vacate the premises immediately!
- **10539**: You received a stamp!
- **10733**: This area is off-limits.
- **10734**: You're here for the stamp hunt, right? Here you go. I wonder why so many adventurers are participating in this thing. But then again, I wouldn't want children running around here, either.
- **15620**: What? A Starlight Celebration present? You came all the way to this decrepit part of town just to give this to me? You've a good heart, friend. Thank you.

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

### Event 32693

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 12 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1E F0 FF FF 7F 1D  00 80 23 21 00            B........#!.   
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0007 [0x1D] PRINT_EVENT_MESSAGE(message_id=15620*)
    → "What? A Starlight Celebration present? You came all the way to this decrepit part of town just to give this to me? You've a good heart, friend. Thank you."
  3: 0x000A [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000B [0x21] END_EVENT
  5: 0x000C [0x00] END_REQSTACK()
```

### Event 55

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         1E F0 FF               ...
0010: FF 7F 1D 01 80 23 21 00                           .....#!.        
```

#### Opcodes

```
  0: 0x000D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0012 [0x1D] PRINT_EVENT_MESSAGE(message_id=10733*)
    → "This area is off-limits."
  2: 0x0015 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0016 [0x21] END_EVENT
  4: 0x0017 [0x00] END_REQSTACK()
```

### Event 85

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0018   |
| Data Size    | 16 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                          42 1E F0 FF FF 7F 1D 02          B.......
0020: 80 23 48 03 80 23 21 00                           .#H..#!.        
```

#### Opcodes

```
  0: 0x0018 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0019 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=10734*)
    → "You're here for the stamp hunt, right? Here you go. I wonder why so many adventurers are participating in this thing. But then again, I wouldn't want children running around here, either."
  3: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0022 [0x48] [System] [10539*]:
    → "You received a stamp!"
  5: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0026 [0x21] END_EVENT
  7: 0x0027 [0x00] END_REQSTACK()
```

### Event 176

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0028   |
| Data Size    | 15 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                          37 04 80 05 80 06 80 07          7.......
0030: 80 1E 0B A0 0E 01 00                              .......         
```

#### Opcodes

```
  0: 0x0028 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-150.414*, z=-41.910*, y=0.000*, direction=225.8°*
  1: 0x0031 [0x1E] EventEntity looks at Mydon (ID: 17735691/0x010EA00B) and starts talking
  2: 0x0036 [0x00] END_REQSTACK()
```

### Event 180

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0037  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      00                                  .        
```

#### Opcodes

```
  0: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          32 08 80 37 09 80 0A 80          2..7....
0040: 0B 80 0C 80 1F 00 0D 80  0E 80 0B 80 1F 01 6F 1E  ..............o.
0050: 71 A0 0E 01 00                                    q....           
```

#### Opcodes

```
  0: 0x0038 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-16.725*, z=32.011*, y=6.999*, direction=145.0°*
  2: 0x0044 [0x1F] MOVE_ENTITY: EventEntity moves to X=-19.233*, Z=31.127*, Y=6.999*
  3: 0x004C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x004E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x004F [0x1E] EventEntity looks at Gabbot (ID: 17735793/0x010EA071) and starts talking
  6: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                32 08 80  1F 00 09 80 0A 80 0B 80       2..........
0060: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0055 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0058 [0x1F] MOVE_ENTITY: EventEntity moves to X=-16.725*, Z=32.011*, Y=6.999*
  2: 0x0060 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0062 [0x00] END_REQSTACK()
```

### Event 182

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0063  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          00                                          .            
```

#### Opcodes

```
  0: 0x0063 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0064   |
| Data Size    | 25 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:             32 08 80 33  01 1F 00 0F 80 10 80 0B      2..3........
0070: 80 1F 01 37 11 80 12 80  0B 80 13 80 00           ...7.........   
```

#### Opcodes

```
  0: 0x0064 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0067 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  2: 0x0069 [0x1F] MOVE_ENTITY: EventEntity moves to X=71.475*, Z=-14.144*, Y=6.999*
  3: 0x0071 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0073 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=70.062*, z=-9.282*, y=6.999*, direction=327.0°*
  5: 0x007C [0x00] END_REQSTACK()
```

### Event 591

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007D  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         00                     .  
```

#### Opcodes

```
  0: 0x007D [0x00] END_REQSTACK()
```

### Event 593

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                            00                   . 
```

#### Opcodes

```
  0: 0x007E [0x00] END_REQSTACK()
```

### Event 598

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x007F    |
| Data Size    | 205 bytes |
| Instructions | 30        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               38                 8
0080: 14 80 BA F0 FF FF 7F 15  80 16 80 0B 80 17 80 46  ...............F
0090: 01 42 45 18 80 F0 FF FF  7F F0 FF FF 7F 73 30 30  .BE..........s00
00A0: 32 06 80 1C 19 80 52 18  80 F0 FF FF 7F F0 FF FF  2.....R.........
00B0: 7F 73 30 30 32 1E F0 FF  FF 7F 6F 70 1D 1A 80 23  .s002.....op...#
00C0: 45 1B 80 F0 FF FF 7F F0  FF FF 7F 66 64 6F 31 06  E..........fdo1.
00D0: 80 1C 1C 80 39 1D 80 80  F0 FF FF 7F 27 0A F0 FF  ....9.......'...
00E0: FF 7F 55 45 1B 80 F0 FF  FF 7F F0 FF FF 7F 66 64  ..UE..........fd
00F0: 69 30 06 80 45 18 80 F0  FF FF 7F F0 FF FF 7F 73  i0..E..........s
0100: 30 30 31 06 80 1C 1C 80  2A 0A F0 FF FF 7F 45 1B  001.....*.....E.
0110: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 31 06 80 1C  .........fdo1...
0120: 1C 80 52 18 80 F0 FF FF  7F F0 FF FF 7F 73 30 30  ..R..........s00
0130: 31 46 00 39 1E 80 45 1B  80 F0 FF FF 7F F0 FF FF  1F.9..E.........
0140: 7F 66 64 69 30 06 80 1C  1C 80 21 00              .fdi0.....!.    
```

#### Opcodes

```
  0: 0x007F [0x38] SET_CLIENT_EVENT_MODE(mode=2*)
  1: 0x0082 [0xBA] SET_ENTITY_POSITION(entity_id=LocalPlayer, pos_x=70.697*, pos_z=-15.938*, pos_y=6.999*, direction=282.1°*)
  2: 0x008F [0x46] CAMERA_CONTROL: Disable user control
  3: 0x0091 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  4: 0x0092 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s002" with entities [LocalPlayer, LocalPlayer], work=[102*, 0*]
  5: 0x00A3 [0x1C] WAIT(240* ticks)
  6: 0x00A6 [0x52] END_LOAD_SCHEDULER: End scheduler "s002" with entities [LocalPlayer, LocalPlayer], work=102*
  7: 0x00B5 [0x1E] EventEntity looks at LocalPlayer and starts talking
  8: 0x00BA [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x00BB [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 10: 0x00BC [0x1D] PRINT_EVENT_MESSAGE(message_id=10466*)
    → "I don't know how you got inside, but that area is off limits. Vacate the premises immediately!"
 11: 0x00BF [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x00C0 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 13: 0x00D1 [0x1C] WAIT(120* ticks)
 14: 0x00D4 [0x39] SET_ENTITY_DIRECTION(direction=13.7°*)
 15: 0x00D7 [0x80] LOAD_WAIT(entity=LocalPlayer)
 16: 0x00DC [0x27] REQ_SET(priority=0x0A, entity_id=LocalPlayer, tag_num=0x55)
 17: 0x00E3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 18: 0x00F4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s001" with entities [LocalPlayer, LocalPlayer], work=[102*, 0*]
 19: 0x0105 [0x1C] WAIT(120* ticks)
 20: 0x0108 [0x2A] GET_REQ_LEVEL(level=10, entity_id=LocalPlayer)
 21: 0x010E [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 22: 0x011F [0x1C] WAIT(120* ticks)
 23: 0x0122 [0x52] END_LOAD_SCHEDULER: End scheduler "s001" with entities [LocalPlayer, LocalPlayer], work=102*
 24: 0x0131 [0x46] CAMERA_CONTROL: Restore default settings
 25: 0x0133 [0x39] SET_ENTITY_DIRECTION(direction=17.1°*)
 26: 0x0136 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 27: 0x0147 [0x1C] WAIT(120* ticks)
 28: 0x014A [0x21] END_EVENT
 29: 0x014B [0x00] END_REQSTACK()
```
