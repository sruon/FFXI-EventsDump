# 17784904 - Borghertz

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Port Jeuno (ID: 246) |
| Block Size       | 416 bytes            |
| Total Events     | 9                    |
| References Count | 33                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [20](#event-20)          | 0x0001       |     22 |              4 |
| [65535.1](#event-655351) | 0x0017       |     37 |              9 |
| [65535.2](#event-655352) | 0x003C       |     28 |              8 |
| [65535.3](#event-655353) | 0x0058       |     13 |              4 |
| [49](#event-49)          | 0x0065       |     84 |             20 |
| [48](#event-48)          | 0x00B9       |     13 |              3 |
| [65535.4](#event-655354) | 0x00C6       |     12 |              4 |
| [65535.5](#event-655355) | 0x00D2       |     22 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF52A0  |  4294922912 |
|       1 | 0x1F2D      |        7981 |
|       2 | 0x1D09      |        7433 |
|       3 | 0x080B      |        2059 |
|       4 | 0x0040      |          64 |
|       5 | 0x0000      |           0 |
|       6 | 0x000D      |          13 |
|       7 | 0xFFFF4C60  |  4294921312 |
|       8 | 0x1F20      |        7968 |
|       9 | 0x1F42      |        8002 |
|      10 | 0xFFFF425F  |  4294918751 |
|      11 | 0x0B75      |        2933 |
|      12 | 0x1F40      |        8000 |
|      13 | 0xFFFF3542  |  4294915394 |
|      14 | 0xFFFFF73E  |  4294965054 |
|      15 | 0x1F3F      |        7999 |
|      16 | 0x0522      |        1314 |
|      17 | 0xFFFF31A7  |  4294914471 |
|      18 | 0xFFFFF332  |  4294964018 |
|      19 | 0xFFFF31F6  |  4294914550 |
|      20 | 0xFFFFE94F  |  4294961487 |
|      21 | 0x0080      |         128 |
|      22 | 0x1B58      |        7000 |
|      23 | 0x0C2E      |        3118 |
|      24 | 0x00D3      |         211 |
|      25 | 0x1C93      |        7315 |
|      26 | 0xFFFF327D  |  4294914685 |
|      27 | 0xFFFFF26F  |  4294963823 |
|      28 | 0xFFFF494F  |  4294920527 |
|      29 | 0x1F4B      |        8011 |
|      30 | 0xFFFF56D7  |  4294923991 |
|      31 | 0x1F74      |        8052 |
|      32 | 0x1ACB      |        6859 |

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

### Event 20

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 6C F8 FF FF 7F 04   7........l.....
0010: 80 05 80 32 06 80 00                              ...2...         
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-44.384*, z=7.981*, y=7.433*, direction=181.0°*
  1: 0x000A [0x6C] FADE_ENTITY_COLOR(entity_id=EventEntity, end_alpha=64*, fade_time=0*)
  2: 0x0013 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x0016 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 37 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      1F  00 07 80 08 80 09 80 1F         .........
0020: 01 6F 4A F8 FF FF 7F F0  FF FF 7F 6F 76 F8 FF FF  .oJ........ov...
0030: 7F 1F 00 0A 80 0B 80 0C  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x0017 [0x1F] MOVE_ENTITY: EventEntity moves to X=-45.984*, Z=7.968*, Y=8.002*
  1: 0x001F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0021 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0022 [0x4A] EventEntity looks at LocalPlayer
  4: 0x002B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x002C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  6: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=-48.545*, Z=2.933*, Y=8.000*
  7: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      37 0D 80 0E              7...
0040: 80 0F 80 10 80 1F 00 11  80 12 80 0F 80 1F 01 6F  ...............o
0050: 1E F0 FF FF 7F 6F 70 00                           .....op.        
```

#### Opcodes

```
  0: 0x003C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-51.902*, z=-2.242*, y=7.999*, direction=115.5°*
  1: 0x0045 [0x1F] MOVE_ENTITY: EventEntity moves to X=-52.825*, Z=-3.278*, Y=7.999*
  2: 0x004D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x004F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0050 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0055 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0056 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  7: 0x0057 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0058   |
| Data Size    | 13 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                          1F 00 13 80 14 80 0F 80          ........
0060: 1F 01 22 01 00                                    .."..           
```

#### Opcodes

```
  0: 0x0058 [0x1F] MOVE_ENTITY: EventEntity moves to X=-52.746*, Z=-5.809*, Y=7.999*
  1: 0x0060 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0062 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x0064 [0x00] END_REQSTACK()
```

### Event 49

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0065   |
| Data Size    | 84 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                42 2F 00  48 60 0F 01 6C 48 60 0F       B/.H`..lH`.
0070: 01 05 80 15 80 33 01 37  13 80 14 80 16 80 17 80  .....3.7........
0080: 33 01 80 F8 FF FF 7F 22  00 6C 48 60 0F 01 04 80  3......".lH`....
0090: 15 80 1E F0 FF FF 7F 6F  70 03 02 10 18 80 2B 48  .......op.....+H
00A0: 60 0F 01 19 80 23 6C 48  60 0F 01 05 80 15 80 92  `....#lH`.......
00B0: 01 F8 FF FF 7F 22 01 21  00                       .....".!.       
```

#### Opcodes

```
  0: 0x0065 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0066 [0x2F] Borghertz (ID: 17784904/0x010F6048)->Render.Flags0 &= ~0x80000 // Bit 19
  2: 0x006C [0x6C] FADE_ENTITY_COLOR(entity_id=Borghertz (ID: 17784904/0x010F6048), end_alpha=0*, fade_time=128*)
  3: 0x0075 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  4: 0x0077 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-52.746*, z=-5.809*, y=7.000*, direction=274.0°*
  5: 0x0080 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  6: 0x0082 [0x80] LOAD_WAIT(entity=EventEntity)
  7: 0x0087 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  8: 0x0089 [0x6C] FADE_ENTITY_COLOR(entity_id=Borghertz (ID: 17784904/0x010F6048), end_alpha=64*, fade_time=128*)
  9: 0x0092 [0x1E] EventEntity looks at LocalPlayer and starts talking
 10: 0x0097 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 11: 0x0098 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 12: 0x0099 [0x03] Work_Zone[2] = 211*
 13: 0x009E [0x2B] Borghertz (ID: 17784904/0x010F6048) [7315*]:
    → "Very well. Bring $6 from Castle Zvahl. Leave them and those gauntlets inside my toolbox, and I shall restore the gauntlets."
 14: 0x00A5 [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x00A6 [0x6C] FADE_ENTITY_COLOR(entity_id=Borghertz (ID: 17784904/0x010F6048), end_alpha=0*, fade_time=128*)
 16: 0x00AF [0x92] EventEntity->Render.Flags3 ^= 0x01
 17: 0x00B5 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
 18: 0x00B7 [0x21] END_EVENT
 19: 0x00B8 [0x00] END_REQSTACK()
```

### Event 48

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             37 13 80 14 80 0F 80           7......
00C0: 17 80 32 06 80 00                                 ..2...          
```

#### Opcodes

```
  0: 0x00B9 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-52.746*, z=-5.809*, y=7.999*, direction=274.0°*
  1: 0x00C2 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x00C5 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C6   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                   1F 00  1A 80 1B 80 0F 80 1F 01        ..........
00D0: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x00C6 [0x1F] MOVE_ENTITY: EventEntity moves to X=-52.611*, Z=-3.473*, Y=7.999*
  1: 0x00CE [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00D0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00D1 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D2   |
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:       1F 00 1C 80 1D 80  09 80 1F 01 6F 1F 00 1E    ..........o...
00E0: 80 1F 80 20 80 1F 01 00                           ... ....        
```

#### Opcodes

```
  0: 0x00D2 [0x1F] MOVE_ENTITY: EventEntity moves to X=-46.769*, Z=8.011*, Y=8.002*
  1: 0x00DA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00DC [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00DD [0x1F] MOVE_ENTITY: EventEntity moves to X=-43.305*, Z=8.052*, Y=6.859*
  4: 0x00E5 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x00E7 [0x00] END_REQSTACK()
```
