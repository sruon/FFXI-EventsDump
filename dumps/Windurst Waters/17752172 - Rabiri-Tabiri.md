# 17752172 - Rabiri-Tabiri

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 184 bytes                 |
| Total Events     | 6                         |
| References Count | 5                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [568](#event-568)        | 0x0030       |     35 |             11 |
| [264](#event-264)        | 0x0053       |     39 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0055      |          85 |
|       1 | 0x001E      |          30 |
|       2 | 0x226E      |        8814 |
|       3 | 0x1EEE      |        7918 |
|       4 | 0x1EEF      |        7919 |

## String References

- **7918**: The food offerings made to the Yagudo are first placed in the two altars in front of each of the cavern entrances in Giddeus.
- **7919**: But if you don't hurry up, the Yagudo will carry them off to their underground treasure chambers for later distribution.
- **8814**: tNanah-nananah!t Before a new dish gets added to the menu at the westaurant over there, we's alweady tasted it! I bet you're jealous, 'coz we're sooo wucky!

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
0000:    5B 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   [..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=85*
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

### Event 568

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 35 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 86 00 F8 FF FF 7F 1E F0  FF FF 7F 6F 70 29 08 6C  ...........op).l
0040: E0 0E 01 01 1D 02 80 23  29 08 6C E0 0E 01 02 20  .......#).l.... 
0050: 00 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0030 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0036 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x003B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x003C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x003D [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rabiri-Tabiri (ID: 17752172/0x010EE06C), tag_num=0x01)
  5: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=8814*)
    → "tNanah-nananah!t Before a new dish gets added to the menu at the westaurant over there, we's alweady tasted it! I bet you're jealous, 'coz we're sooo wucky!"
  6: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0048 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rabiri-Tabiri (ID: 17752172/0x010EE06C), tag_num=0x02)
  8: 0x004F [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x0051 [0x21] END_EVENT
 10: 0x0052 [0x00] END_REQSTACK()
```

### Event 264

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0053   |
| Data Size    | 39 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:          86 00 F8 FF FF  7F 1E F0 FF FF 7F 6F 70     ...........op
0060: 29 08 6C E0 0E 01 01 1D  03 80 23 1D 04 80 23 29  ).l.......#...#)
0070: 08 6C E0 0E 01 02 20 00  21 00                    .l.... .!.      
```

#### Opcodes

```
  0: 0x0053 [0x86] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0059 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x005E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x005F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0060 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rabiri-Tabiri (ID: 17752172/0x010EE06C), tag_num=0x01)
  5: 0x0067 [0x1D] PRINT_EVENT_MESSAGE(message_id=7918*)
    → "The food offerings made to the Yagudo are first placed in the two altars in front of each of the cavern entrances in Giddeus."
  6: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x006B [0x1D] PRINT_EVENT_MESSAGE(message_id=7919*)
    → "But if you don't hurry up, the Yagudo will carry them off to their underground treasure chambers for later distribution."
  8: 0x006E [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x006F [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Rabiri-Tabiri (ID: 17752172/0x010EE06C), tag_num=0x02)
 10: 0x0076 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0078 [0x21] END_EVENT
 12: 0x0079 [0x00] END_REQSTACK()
```
