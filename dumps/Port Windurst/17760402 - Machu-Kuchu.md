# 17760402 - Machu-Kuchu

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 244 bytes               |
| Total Events     | 4                       |
| References Count | 11                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [338](#event-338)        | 0x0027       |    128 |             25 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x101F      |        4127 |
|       3 | 0x1020      |        4128 |
|       4 | 0x1021      |        4129 |
|       5 | 0x0001      |           1 |
|       6 | 0x0000      |           0 |
|       7 | 0x0105      |         261 |
|       8 | 0x00C8      |         200 |
|       9 | 0x0078      |         120 |
|      10 | 0x0002      |           2 |

## String References

- **4127**: Have you, traveler, also come to Windurst to take a looky at the Great Star Tree? If so, then the star tree, also known as Heavens Tower, is far to the northeasty of here, in Windurst Walls.
- **4128**: If you wanty, I can use my magic to sendy you to Windurst Walls in an instant. Would you likey that?
- **4129**: Warpy to Windurst Walls? [Yes./No.]

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 338

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0027    |
| Data Size    | 128 bytes |
| Instructions | 25        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      1E  F0 FF FF 7F 6F 70 29 08         .....op).
0030: 92 00 0F 01 01 1D 02 80  23 1D 03 80 23 66 00 80  ........#...#f..
0040: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 24 04 80 05  ........tlk1$...
0050: 80 06 80 25 02 00 10 06  80 00 93 00 53 F8 FF FF  ...%........S...
0060: 7F F8 FF FF 7F 74 6C 6B  31 73 07 80 F8 FF FF 7F  .....tlk1s......
0070: F0 FF FF 7F 1C 08 80 45  08 80 F8 FF FF 7F F8 FF  .......E........
0080: FF 7F 66 64 6F 32 06 80  1C 09 80 03 01 10 05 80  ..fdo2..........
0090: 01 A3 00 02 00 10 05 80  00 A3 00 03 01 10 0A 80  ................
00A0: 01 A3 00 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x0027 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x002D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002E [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Machu-Kuchu (ID: 17760402/0x010F0092), tag_num=0x01)
  4: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=4127*)
    → "Have you, traveler, also come to Windurst to take a looky at the Great Star Tree? If so, then the star tree, also known as Heavens Tower, is far to the northeasty of here, in Windurst Walls."
  5: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=4128*)
    → "If you wanty, I can use my magic to sendy you to Windurst Walls in an instant. Would you likey that?"
  7: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  9: 0x004C [0x24] CREATE_DIALOG(message_id=4129*, default_option=1*, option_flags=0*)
    → "Warpy to Windurst Walls? [Yes./No.]"
 10: 0x0053 [0x25] WAIT_DIALOG_SELECT()
 11: 0x0054 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0093
 12: 0x005C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 13: 0x0069 [0x73] EventEntity casts magic 261* on LocalPlayer
 14: 0x0074 [0x1C] WAIT(200* ticks)
 15: 0x0077 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [EventEntity, EventEntity], work=[200*, 0*]
 16: 0x0088 [0x1C] WAIT(120* ticks)
 17: 0x008B [0x03] Work_Zone[1] = 1*
 18: 0x0090 [0x01] GOTO 0x00A3
 19: 0x0093 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x00A3
 20: 0x009B [0x03] Work_Zone[1] = 2*
 21: 0x00A0 [0x01] GOTO 0x00A3

SUBROUTINE_00A3:
 22: 0x00A3 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 23: 0x00A5 [0x21] END_EVENT
 24: 0x00A6 [0x00] END_REQSTACK()
```
