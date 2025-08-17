# 17727568 - Bonarpant

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 316 bytes                 |
| Total Events     | 8                         |
| References Count | 13                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [4](#event-4)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     32 |              7 |
| [65535.2](#event-655352) | 0x0022       |     23 |              7 |
| [65535.3](#event-655353) | 0x0039       |     81 |             16 |
| [595](#event-595)        | 0x008A       |     43 |             13 |
| [65535.4](#event-655354) | 0x00B5       |     16 |              2 |
| [65535.5](#event-655355) | 0x00C5       |     19 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFF5989  |  4294924681 |
|       2 | 0xFFFF96D5  |  4294940373 |
|       3 | 0xFFFFF060  |  4294963296 |
|       4 | 0x0104      |         260 |
|       5 | 0x07D0      |        2000 |
|       6 | 0xFFFF5C6A  |  4294925418 |
|       7 | 0xFFFF67E3  |  4294928355 |
|       8 | 0x0014      |          20 |
|       9 | 0x1EDE      |        7902 |
|      10 | 0x001E      |          30 |
|      11 | 0x1EDF      |        7903 |
|      12 | 0x003C      |          60 |

## String References

- **7902**: It seems everyone is worried about the Orcs these days. Something's going on, that's for certain!
- **7903**: It's about time we marched on their camps, I say. We've put up with those Orcs long enough! We Elvaan must put them back in their place.

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

### Event 4

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 32 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       22 01 92 01 F8 FF  FF 7F 94 01 F8 FF FF 7F    ".............
0010: 32 00 80 37 01 80 02 80  03 80 04 80 1E 70 80 0E  2..7.........p..
0020: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0002 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0004 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000A [0x94] EventEntity->Render.Flags3 ^= 0x01
  3: 0x0010 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  4: 0x0013 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-42.615*, z=-26.923*, y=-4.000*, direction=22.9°*
  5: 0x001C [0x1E] EventEntity looks at Ulmia (ID: 17727600/0x010E8070) and starts talking
  6: 0x0021 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0022   |
| Data Size    | 23 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:       03 00 00 05 80 1A  46 00 32 00 80 1F 00 01    ......F.2.....
0030: 00 02 00 03 00 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x0022 [0x03] ExtData[1]->WorkLocal[0] = 2000*
  1: 0x0027 [0x1A] CALL_SUBROUTINE(address=0x0046)
  2: 0x002A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=ExtData[1]->WorkLocal[1], Z=ExtData[1]->WorkLocal[2], Y=ExtData[1]->WorkLocal[3]
  4: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0037 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0038 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0039   |
| Data Size    | 81 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                             1F 00 06 80 07 80 03           .......
0040: 80 1F 01 22 01 00 3B F8  FF FF 7F 01 00 02 00 03  ..."..;.........
0050: 00 3A F8 FF FF 7F 04 00  17 05 00 04 00 00 00 16  .:..............
0060: 06 00 04 00 00 00 07 01  00 05 00 07 02 00 06 00  ................
0070: 1B 17 05 00 04 00 00 00  16 06 00 04 00 00 00 07  ................
0080: 01 00 05 00 07 02 00 06  00 1B                    ..........      
```

#### Opcodes

```
  0: 0x0039 [0x1F] MOVE_ENTITY: EventEntity moves to X=-41.878*, Z=-38.941*, Y=-4.000*
  1: 0x0041 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0043 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  3: 0x0045 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0046 [0x3B] GET_ENTITY_POSITION(entity=EventEntity, x_destination=ExtData[1]->WorkLocal[1], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[3])
     0x0051 [0x3A] CONVERT_YAW_TO_BYTE(entity=EventEntity, result_destination=ExtData[1]->WorkLocal[4])
     0x0058 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x005F [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0066 [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x006B [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0070 [0x1B] RETURN
     0x0071 [0x17] ExtData[1]->WorkLocal[5] = cos(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x0078 [0x16] ExtData[1]->WorkLocal[6] = sin(ExtData[1]->WorkLocal[4]) * ExtData[1]->WorkLocal[0]
     0x007F [0x07] ExtData[1]->WorkLocal[1] += ExtData[1]->WorkLocal[5]
     0x0084 [0x07] ExtData[1]->WorkLocal[2] += ExtData[1]->WorkLocal[6]
     0x0089 [0x1B] RETURN
```

### Event 595

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008A   |
| Data Size    | 43 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                1E F0 FF FF 7F 6F            .....o
0090: 70 66 08 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  pf..........tlk0
00A0: 1D 09 80 23 1C 0A 80 1D  0B 80 23 5E 69 64 6C 30  ...#......#^idl0
00B0: 1C 0A 80 21 00                                    ...!.           
```

#### Opcodes

```
  0: 0x008A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x008F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0090 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0091 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  4: 0x00A0 [0x1D] PRINT_EVENT_MESSAGE(message_id=7902*)
    → "It seems everyone is worried about the Orcs these days. Something's going on, that's for certain!"
  5: 0x00A3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00A4 [0x1C] WAIT(30* ticks)
  7: 0x00A7 [0x1D] PRINT_EVENT_MESSAGE(message_id=7903*)
    → "It's about time we marched on their camps, I say. We've put up with those Orcs long enough! We Elvaan must put them back in their place."
  8: 0x00AA [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x00AB [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 10: 0x00B0 [0x1C] WAIT(30* ticks)
 11: 0x00B3 [0x21] END_EVENT
 12: 0x00B4 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B5   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                66 08 80  F8 FF FF 7F F8 FF FF 7F       f..........
00C0: 74 6C 6B 30 00                                    tlk0.           
```

#### Opcodes

```
  0: 0x00B5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  1: 0x00C4 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C5   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                66 08 80  F8 FF FF 7F F8 FF FF 7F       f..........
00D0: 74 6C 6B 31 1C 0C 80 00                           tlk1....        
```

#### Opcodes

```
  0: 0x00C5 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  1: 0x00D4 [0x1C] WAIT(60* ticks)
  2: 0x00D7 [0x00] END_REQSTACK()
```
