# 17752179 - Funpo-Shipo

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 200 bytes                 |
| Total Events     | 6                         |
| References Count | 7                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [576](#event-576)        | 0x0030       |     39 |             13 |
| [938](#event-938)        | 0x0057       |     43 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x2279      |        8825 |
|       3 | 0x227A      |        8826 |
|       4 | 0x2FFE      |       12286 |
|       5 | 0x3005      |       12293 |
|       6 | 0x3006      |       12294 |

## String References

- **8825**: Among the guards of Windurst are the automatons who speaky-weaky in the words of the stars.
- **8826**: They are the Cardians, magical puppet-like dolly-wollys that are made at the Manustery.
- **12286**: <Player>'s badge flashes brightly.
- **12293**: Among the guards of Windurst are the automatons who speaky-weaky in the words of the stars.
- **12294**: I heardy-weardy that there are automatons in Aht Urhgan too, but they can't do what ours can! Talk about boring-woring!

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

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5E  69 64 6C 30 1C 01 80 00         ^idl0....
```

#### Opcodes

```
  0: 0x0027 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x002C [0x1C] WAIT(30* ticks)
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 576

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 86 00 F8 FF FF 7F 1E F0  FF FF 7F 6F 70 29 08 73  ...........op).s
0040: E0 0E 01 01 1D 02 80 23  1D 03 80 23 29 08 73 E0  .......#...#).s.
0050: 0E 01 02 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x0030 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0036 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x003B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x003C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x003D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Funpo-Shipo (ID: 17752179/0x010EE073), tag_num=0x01)
  5: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=8825*)
    → "Among the guards of Windurst are the automatons who speaky-weaky in the words of the stars."
  6: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0048 [0x1D] PRINT_EVENT_MESSAGE(message_id=8826*)
    → "They are the Cardians, magical puppet-like dolly-wollys that are made at the Manustery."
  8: 0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x004C [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Funpo-Shipo (ID: 17752179/0x010EE073), tag_num=0x02)
 10: 0x0053 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0055 [0x21] END_EVENT
 12: 0x0056 [0x00] END_REQSTACK()
```

### Event 938

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 43 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      42  48 04 80 86 00 F8 FF FF         BH.......
0060: 7F 1E F0 FF FF 7F 6F 70  29 08 73 E0 0E 01 01 1D  ......op).s.....
0070: 05 80 23 1D 06 80 23 29  08 73 E0 0E 01 02 20 00  ..#...#).s.... .
0080: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0057 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0058 [0x48] [System] [12286*]:
    → "<Player>'s badge flashes brightly."
  2: 0x005B [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  3: 0x0061 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0066 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0067 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  6: 0x0068 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Funpo-Shipo (ID: 17752179/0x010EE073), tag_num=0x01)
  7: 0x006F [0x1D] PRINT_EVENT_MESSAGE(message_id=12293*)
    → "Among the guards of Windurst are the automatons who speaky-weaky in the words of the stars."
  8: 0x0072 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0073 [0x1D] PRINT_EVENT_MESSAGE(message_id=12294*)
    → "I heardy-weardy that there are automatons in Aht Urhgan too, but they can't do what ours can! Talk about boring-woring!"
 10: 0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0077 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Funpo-Shipo (ID: 17752179/0x010EE073), tag_num=0x02)
 12: 0x007E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x0080 [0x21] END_EVENT
 14: 0x0081 [0x00] END_REQSTACK()
```
