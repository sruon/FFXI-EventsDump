# 17142601 - Zharijarl

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Grauberg [S] (ID: 89) |
| Block Size       | 408 bytes             |
| Total Events     | 14                    |
| References Count | 39                    |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [17](#event-17)            | 0x0001       |      1 |              1 |
| [18](#event-18)            | 0x0002       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0003       |     22 |              3 |
| [65535.2](#event-655352)   | 0x0019       |     14 |              4 |
| [65535.3](#event-655353)   | 0x0027       |     14 |              4 |
| [65535.4](#event-655354)   | 0x0035       |     14 |              4 |
| [65535.5](#event-655355)   | 0x0043       |     14 |              4 |
| [65535.6](#event-655356)   | 0x0051       |     14 |              4 |
| [65535.7](#event-655357)   | 0x005F       |     24 |              3 |
| [65535.8](#event-655358)   | 0x0077       |     15 |              5 |
| [65535.9](#event-655359)   | 0x0086       |     15 |              5 |
| [65535.10](#event-6553510) | 0x0095       |     15 |              5 |
| [65535.11](#event-6553511) | 0x00A4       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0x002E      |          46 |
|       3 | 0x00B0      |         176 |
|       4 | 0x0012      |          18 |
|       5 | 0xFFF80161  |  4294443361 |
|       6 | 0x38EEB     |      233195 |
|       7 | 0xFFFD6270  |  4294795888 |
|       8 | 0x000C      |          12 |
|       9 | 0xFFF834DF  |  4294456543 |
|      10 | 0x30BD4     |      199636 |
|      11 | 0xFFFD6BFD  |  4294798333 |
|      12 | 0xFFFDBA85  |  4294818437 |
|      13 | 0xFFFA888D  |  4294609037 |
|      14 | 0xFFFFA7B3  |  4294944691 |
|      15 | 0x0013      |          19 |
|      16 | 0xFFFD9017  |  4294807575 |
|      17 | 0xFFFA9B98  |  4294613912 |
|      18 | 0xFFFFA2CF  |  4294943439 |
|      19 | 0x0028      |          40 |
|      20 | 0xFFFD8CEC  |  4294806764 |
|      21 | 0xFFFA99C2  |  4294613442 |
|      22 | 0xFFFFA257  |  4294943319 |
|      23 | 0x0005      |           5 |
|      24 | 0x00CA      |         202 |
|      25 | 0x0038      |          56 |
|      26 | 0xFFFD87A2  |  4294805410 |
|      27 | 0xFFFA94F2  |  4294612210 |
|      28 | 0xFFFFA0AB  |  4294942891 |
|      29 | 0xFFFD8BC0  |  4294806464 |
|      30 | 0xFFFAA1CB  |  4294615499 |
|      31 | 0xFFFFA293  |  4294943379 |
|      32 | 0xFFFDECAC  |  4294831276 |
|      33 | 0xFFFB3C40  |  4294655040 |
|      34 | 0xFFFFB3CF  |  4294947791 |
|      35 | 0x002C      |          44 |
|      36 | 0xFFFE8523  |  4294870307 |
|      37 | 0xFFFC259B  |  4294714779 |
|      38 | 0xFFFF913F  |  4294938943 |

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

### Event 17

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

### Event 18

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 22 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          96 B6 0B 00 80  00 80 01 80 02 80 03 80     .............
0010: 03 80 03 80 01 80 01 80  00                       .........       
```

#### Opcodes

```
  0: 0x0003 [0x96] UNSET_EVENT_NPC: Restore NPC after event (removes event NPC status)
  1: 0x0004 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=1*, head=0*, body=46*, hands=176*, legs=176*, feet=176*, main=0*, sub=0*)
  2: 0x0018 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             32 04 80 1F 00 05 80           2......
0020: 06 80 07 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0019 [0x32] ExtData[1]->MainSpeed = 18* * 0.1
  1: 0x001C [0x1F] MOVE_ENTITY: EventEntity moves to X=-523.935*, Z=233.195*, Y=-171.408*
  2: 0x0024 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      32  08 80 5A 00 09 80 0A 80         2..Z.....
0030: 0B 80 5A 01 00                                    ..Z..           
```

#### Opcodes

```
  0: 0x0027 [0x32] ExtData[1]->MainSpeed = 12* * 0.1
  1: 0x002A [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-510.753*, Z=199.636*, Y=-168.963*
  2: 0x0032 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                32 08 80  5A 00 0C 80 0D 80 0E 80       2..Z.......
0040: 5A 01 00                                          Z..             
```

#### Opcodes

```
  0: 0x0035 [0x32] ExtData[1]->MainSpeed = 12* * 0.1
  1: 0x0038 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-148.859*, Z=-358.259*, Y=-22.605*
  2: 0x0040 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0042 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0043   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          32 0F 80 5A 00  10 80 11 80 12 80 5A 01     2..Z.......Z.
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0043 [0x32] ExtData[1]->MainSpeed = 19* * 0.1
  1: 0x0046 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-159.721*, Z=-353.384*, Y=-23.857*
  2: 0x004E [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0050 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    32 13 80 5A 00 14 80  15 80 16 80 5A 01 00      2..Z.......Z.. 
```

#### Opcodes

```
  0: 0x0051 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0054 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-160.532*, Z=-353.854*, Y=-23.977*
  2: 0x005C [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x005E [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 24 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               95                 .
0060: 01 80 B6 0B 00 80 17 80  17 80 17 80 17 80 17 80  ................
0070: 17 80 18 80 01 80 00                              .......         
```

#### Opcodes

```
  0: 0x005F [0x95] SETUP_EVENT_NPC: Prepare NPC for event (Render.Flags3 = 0*)
  1: 0x0062 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=1*, hair=5*, head=5*, body=5*, hands=5*, legs=5*, feet=5*, main=202*, sub=0*)
  2: 0x0076 [0x00] END_REQSTACK()
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
0070:                      32  19 80 1F 00 1A 80 1B 80         2........
0080: 1C 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0077 [0x32] ExtData[1]->MainSpeed = 56* * 0.1
  1: 0x007A [0x1F] MOVE_ENTITY: EventEntity moves to X=-161.886*, Z=-355.086*, Y=-24.405*
  2: 0x0082 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0084 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   32 19  80 1F 00 1D 80 1E 80 1F        2.........
0090: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0086 [0x32] ExtData[1]->MainSpeed = 56* * 0.1
  1: 0x0089 [0x1F] MOVE_ENTITY: EventEntity moves to X=-160.832*, Z=-351.797*, Y=-23.917*
  2: 0x0091 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0093 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0094 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0095   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                32 19 80  1F 00 20 80 21 80 22 80       2.... .!.".
00A0: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0095 [0x32] ExtData[1]->MainSpeed = 56* * 0.1
  1: 0x0098 [0x1F] MOVE_ENTITY: EventEntity moves to X=-136.020*, Z=-312.256*, Y=-19.505*
  2: 0x00A0 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00A2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00A3 [0x00] END_REQSTACK()
```

### Event 65535.11

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A4   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:             32 23 80 5A  00 24 80 25 80 26 80 5A      2#.Z.$.%.&.Z
00B0: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x00A4 [0x32] ExtData[1]->MainSpeed = 44* * 0.1
  1: 0x00A7 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-96.989*, Z=-252.517*, Y=-28.353*
  2: 0x00AF [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x00B1 [0x00] END_REQSTACK()
```
