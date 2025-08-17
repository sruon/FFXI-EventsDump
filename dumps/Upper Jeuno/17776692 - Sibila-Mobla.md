# 17776692 - Sibila-Mobla

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 252 bytes             |
| Total Events     | 11                    |
| References Count | 14                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [98](#event-98)          | 0x0001       |     13 |              7 |
| [33](#event-33)          | 0x000E       |      3 |              2 |
| [10083](#event-10083)    | 0x0011       |     22 |             10 |
| [10151](#event-10151)    | 0x0027       |      7 |              2 |
| [10209](#event-10209)    | 0x002E       |      7 |              2 |
| [10210](#event-10210)    | 0x0035       |      7 |              2 |
| [10211](#event-10211)    | 0x003C       |      7 |              2 |
| [10149](#event-10149)    | 0x0043       |      7 |              2 |
| [65535.1](#event-655351) | 0x004A       |     34 |              8 |
| [65535.2](#event-655352) | 0x006C       |     28 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1DD6      |        7638 |
|       1 | 0x2B70      |       11120 |
|       2 | 0x001E      |          30 |
|       3 | 0x2B71      |       11121 |
|       4 | 0x2B72      |       11122 |
|       5 | 0x0384      |         900 |
|       6 | 0x0001      |           1 |
|       7 | 0x0028      |          40 |
|       8 | 0xFFFF1BE4  |  4294908900 |
|       9 | 0x18B42     |      101186 |
|      10 | 0x0000      |           0 |
|      11 | 0x027F      |         639 |
|      12 | 0xFFFF29E8  |  4294912488 |
|      13 | 0x193E9     |      103401 |

## String References

- **7638**: Move itaru! I want to join the Ducal Guards! Must...march...more...
- **11120**: <Player>'s badge flashes brightly.
- **11121**: Huff...puff... I'm trying to buildy-wuild some muscle so I can join the Ducal Guards, but whew! This is a lotta work!
- **11122**: Puff...huff... Mercenaries fight on the very fwont lines, so I bet they hafta be weaaally tough! Their twaining must be even worse!

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

### Event 98

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 21 00         .....op...#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=7638*)
    → "Move itaru! I want to join the Ducal Guards! Must...march...more..."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000E  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            22 01                ".
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x000E [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 10083

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    42 48 01 80 1E F0 FF  FF 7F 1C 02 80 1D 03 80   BH.............
0020: 23 1D 04 80 23 21 00                              #...#!.         
```

#### Opcodes

```
  0: 0x0011 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0012 [0x48] [System] [11120*]:
    → "<Player>'s badge flashes brightly."
  2: 0x0015 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x001A [0x1C] WAIT(30* ticks)
  4: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=11121*)
    → "Huff...puff... I'm trying to buildy-wuild some muscle so I can join the Ducal Guards, but whew! This is a lotta work!"
  5: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0021 [0x1D] PRINT_EVENT_MESSAGE(message_id=11122*)
    → "Puff...huff... Mercenaries fight on the very fwont lines, so I bet they hafta be weaaally tough! Their twaining must be even worse!"
  7: 0x0024 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0025 [0x21] END_EVENT
  9: 0x0026 [0x00] END_REQSTACK()
```

### Event 10151

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      92  01 F8 FF FF 7F 00               .......  
```

#### Opcodes

```
  0: 0x0027 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x002D [0x00] END_REQSTACK()
```

### Event 10209

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x002E  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                            92 01                ..
0030: F8 FF FF 7F 00                                    .....           
```

#### Opcodes

```
  0: 0x002E [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0034 [0x00] END_REQSTACK()
```

### Event 10210

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0035  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                92 01 F8  FF FF 7F 00                   .......    
```

#### Opcodes

```
  0: 0x0035 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x003B [0x00] END_REQSTACK()
```

### Event 10211

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x003C  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      92 01 F8 FF              ....
0040: FF 7F 00                                          ...             
```

#### Opcodes

```
  0: 0x003C [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0042 [0x00] END_REQSTACK()
```

### Event 10149

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0043  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:          92 01 F8 FF FF  7F 00                       .......      
```

#### Opcodes

```
  0: 0x0043 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                1C 05 80 03 2F 10            ..../.
0050: 06 80 32 07 80 1F 00 08  80 09 80 0A 80 1F 01 03  ..2.............
0060: 28 10 06 80 4B 34 40 0F  01 0B 80 00              (...K4@.....    
```

#### Opcodes

```
  0: 0x004A [0x1C] WAIT(900* ticks)
  1: 0x004D [0x03] Work_Zone[47] = 1*
  2: 0x0052 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x0055 [0x1F] MOVE_ENTITY: EventEntity moves to X=-58.396*, Z=101.186*, Y=0.000*
  4: 0x005D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x005F [0x03] Work_Zone[40] = 1*
  6: 0x0064 [0x4B] UPDATE_ENTITY_YAW(entity=Sibila-Mobla (ID: 17776692/0x010F4034), yaw=3.5°*)
  7: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 28 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      32 07 80 1F              2...
0070: 00 0C 80 0D 80 0A 80 1F  01 4B 34 40 0F 01 0B 80  .........K4@....
0080: 27 05 34 40 0F 01 09 00                           '.4@....        
```

#### Opcodes

```
  0: 0x006C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x006F [0x1F] MOVE_ENTITY: EventEntity moves to X=-54.808*, Z=103.401*, Y=0.000*
  2: 0x0077 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0079 [0x4B] UPDATE_ENTITY_YAW(entity=Sibila-Mobla (ID: 17776692/0x010F4034), yaw=3.5°*)
  4: 0x0080 [0x27] REQ_SET(priority=0x05, entity_id=Sibila-Mobla (ID: 17776692/0x010F4034), tag_num=0x09)
  5: 0x0087 [0x00] END_REQSTACK()
```
