# 17776646 - Panta-Putta

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 288 bytes             |
| Total Events     | 9                     |
| References Count | 15                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      6 |              3 |
| [33](#event-33)          | 0x0006       |     10 |              2 |
| [65535.1](#event-655351) | 0x0010       |     40 |             10 |
| [65535.2](#event-655352) | 0x0038       |     67 |             11 |
| [34](#event-34)          | 0x007B       |     10 |              2 |
| [65535.3](#event-655353) | 0x0085       |     29 |              3 |
| [65535.4](#event-655354) | 0x00A2       |      9 |              3 |
| [65535.5](#event-655355) | 0x00AB       |      4 |              2 |
| [65535.6](#event-655356) | 0x00AF       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0007      |           7 |
|       1 | 0xFFFF1C68  |  4294909032 |
|       2 | 0xFFFFF0FC  |  4294963452 |
|       3 | 0xFFFFFE0C  |  4294966796 |
|       4 | 0x0369      |         873 |
|       5 | 0x0015      |          21 |
|       6 | 0xFFFF1DD4  |  4294909396 |
|       7 | 0xFFFFECE7  |  4294962407 |
|       8 | 0xFFFF1452  |  4294906962 |
|       9 | 0xFFFFE5C0  |  4294960576 |
|      10 | 0xFFFF114B  |  4294906187 |
|      11 | 0xFFFFE52A  |  4294960426 |
|      12 | 0x06DA      |        1754 |
|      13 | 0x0055      |          85 |
|      14 | 0x003C      |          60 |

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
0000: 32 00 80 22 01 00                                 2.."..          
```

#### Opcodes

```
  0: 0x0000 [0x32] ExtData[1]->MainSpeed = 7* * 0.1
  1: 0x0003 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  2: 0x0005 [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0006   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   37 01  80 02 80 03 80 04 80 00        7.........
```

#### Opcodes

```
  0: 0x0006 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-58.264*, z=-3.844*, y=-0.500*, direction=76.7°*
  1: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 40 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 32 05 80 1F 00 06 80 07  80 03 80 1F 01 6F 4A F0  2............oJ.
0020: FF FF 7F 06 40 0F 01 4A  01 40 0F 01 06 40 0F 01  ....@..J.@...@..
0030: 1E 05 40 0F 01 6F 70 00                           ..@..op.        
```

#### Opcodes

```
  0: 0x0010 [0x32] ExtData[1]->MainSpeed = 21* * 0.1
  1: 0x0013 [0x1F] MOVE_ENTITY: EventEntity moves to X=-57.900*, Z=-4.889*, Y=-0.500*
  2: 0x001B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001E [0x4A] LocalPlayer looks at Panta-Putta (ID: 17776646/0x010F4006)
  5: 0x0027 [0x4A] Monberaux (ID: 17776641/0x010F4001) looks at Panta-Putta (ID: 17776646/0x010F4006)
  6: 0x0030 [0x1E] EventEntity looks at Two of Swords (ID: 17776645/0x010F4005) and starts talking
  7: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  8: 0x0036 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  9: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 67 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          1F 00 08 80 09 80 03 80          ........
0040: 1F 01 4A F0 FF FF 7F 06  40 0F 01 4A 01 40 0F 01  ..J.....@..J.@..
0050: 06 40 0F 01 1F 00 0A 80  0B 80 03 80 1F 01 6F 4A  .@............oJ
0060: F0 FF FF 7F 06 40 0F 01  4A 01 40 0F 01 06 40 0F  .....@..J.@...@.
0070: 01 4A 06 40 0F 01 05 40  0F 01 00                 .J.@...@...     
```

#### Opcodes

```
  0: 0x0038 [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.334*, Z=-6.720*, Y=-0.500*
  1: 0x0040 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0042 [0x4A] LocalPlayer looks at Panta-Putta (ID: 17776646/0x010F4006)
  3: 0x004B [0x4A] Monberaux (ID: 17776641/0x010F4001) looks at Panta-Putta (ID: 17776646/0x010F4006)
  4: 0x0054 [0x1F] MOVE_ENTITY: EventEntity moves to X=-61.109*, Z=-6.870*, Y=-0.500*
  5: 0x005C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x005E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  7: 0x005F [0x4A] LocalPlayer looks at Panta-Putta (ID: 17776646/0x010F4006)
  8: 0x0068 [0x4A] Monberaux (ID: 17776641/0x010F4001) looks at Panta-Putta (ID: 17776646/0x010F4006)
  9: 0x0071 [0x4A] Panta-Putta (ID: 17776646/0x010F4006) looks at Two of Swords (ID: 17776645/0x010F4005)
 10: 0x007A [0x00] END_REQSTACK()
```

### Event 34

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007B   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                   37 06 80 07 80             7....
0080: 03 80 0C 80 00                                    .....           
```

#### Opcodes

```
  0: 0x007B [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-57.900*, z=-4.889*, y=-0.500*, direction=154.2°*
  1: 0x0084 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0085   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                5B 0D 80  F8 FF FF 7F F8 FF FF 7F       [..........
0090: 74 6C 6B 30 53 F8 FF FF  7F F8 FF FF 7F 74 6C 6B  tlk0S........tlk
00A0: 30 00                                             0.              
```

#### Opcodes

```
  0: 0x0085 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0094 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x00A1 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A2  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:       5E 69 64 6C 30 1C  0E 80 00                   ^idl0....     
```

#### Opcodes

```
  0: 0x00A2 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00A7 [0x1C] WAIT(60* ticks)
  2: 0x00AA [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AB  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                   1C 0E 80 00                .... 
```

#### Opcodes

```
  0: 0x00AB [0x1C] WAIT(60* ticks)
  1: 0x00AE [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00AF  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                               00                 .
```

#### Opcodes

```
  0: 0x00AF [0x00] END_REQSTACK()
```
