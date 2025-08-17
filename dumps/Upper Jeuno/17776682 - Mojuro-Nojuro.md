# 17776682 - Mojuro-Nojuro

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 204 bytes             |
| Total Events     | 4                     |
| References Count | 9                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [128](#event-128)     | 0x0001       |     44 |             12 |
| [10013](#event-10013) | 0x002D       |     42 |             13 |
| [10014](#event-10014) | 0x0057       |     46 |             15 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x1DB3      |        7603 |
|       2 | 0x1DB4      |        7604 |
|       3 | 0x003C      |          60 |
|       4 | 0x2108      |        8456 |
|       5 | 0x2109      |        8457 |
|       6 | 0x213A      |        8506 |
|       7 | 0x213B      |        8507 |
|       8 | 0x213C      |        8508 |

## String References

- **7603**: You know, this pub's got different requirements to get in every day. Like on Tarutaru Day, only Tarutaru can get intaru!
- **7604**: So whenever you're there, you can talk with your peers... You know? I always have a blast, so try it outaru!
- **8456**: A beautiful lady justaru ran that way, tears streaming down her face. I've never seen anything like it.
- **8457**: Today is Tarutaru day at the pub, and she was an Elvaan. I can understand how that'd make you want to cry.
- **8506**: I hear this pub is sometimes reserved by the head of the Tenshodo.
- **8507**: Not a momentaru ago, there were Mithra and Galka and all sorts filing out the door. They were saying something about going to Movalpolos.
- **8508**: Are they thinking of bringing their beastmen buddies back here? Next thing you know, they'll be having "Goblin's Day."

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

### Event 128

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 44 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 76  F8 FF FF 7F 66 00 80 F8   .....ov....f...
0010: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 01 80 23 1D  .......tlk0...#.
0020: 02 80 23 5E 69 64 6C 30  1C 03 80 21 00           ..#^idl0...!.   
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until EventEntity Render.Flags0 and Render.Flags3 conditions are met
  3: 0x000C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=7603*)
    → "You know, this pub's got different requirements to get in every day. Like on Tarutaru Day, only Tarutaru can get intaru!"
  5: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=7604*)
    → "So whenever you're there, you can talk with your peers... You know? I always have a blast, so try it outaru!"
  7: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0023 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  9: 0x0028 [0x1C] WAIT(60* ticks)
 10: 0x002B [0x21] END_EVENT
 11: 0x002C [0x00] END_REQSTACK()
```

### Event 10013

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 42 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         1E F0 FF               ...
0030: FF 7F 6F 70 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..opf..........t
0040: 6C 6B 30 1D 04 80 23 1D  05 80 23 5E 69 64 6C 30  lk0...#...#^idl0
0050: 1C 03 80 20 00 21 00                              ... .!.         
```

#### Opcodes

```
  0: 0x002D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0032 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0033 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0034 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x0043 [0x1D] PRINT_EVENT_MESSAGE(message_id=8456*)
    → "A beautiful lady justaru ran that way, tears streaming down her face. I've never seen anything like it."
  5: 0x0046 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=8457*)
    → "Today is Tarutaru day at the pub, and she was an Elvaan. I can understand how that'd make you want to cry."
  7: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x004B [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  9: 0x0050 [0x1C] WAIT(60* ticks)
 10: 0x0053 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 11: 0x0055 [0x21] END_EVENT
 12: 0x0056 [0x00] END_REQSTACK()
```

### Event 10014

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 46 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      1E  F0 FF FF 7F 6F 70 66 00         .....opf.
0060: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 06 80  .........tlk0...
0070: 23 1D 07 80 23 1D 08 80  23 5E 69 64 6C 30 1C 03  #...#...#^idl0..
0080: 80 20 00 21 00                                    . .!.           
```

#### Opcodes

```
  0: 0x0057 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x005C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x005D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x005E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x006D [0x1D] PRINT_EVENT_MESSAGE(message_id=8506*)
    → "I hear this pub is sometimes reserved by the head of the Tenshodo."
  5: 0x0070 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0071 [0x1D] PRINT_EVENT_MESSAGE(message_id=8507*)
    → "Not a momentaru ago, there were Mithra and Galka and all sorts filing out the door. They were saying something about going to Movalpolos."
  7: 0x0074 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0075 [0x1D] PRINT_EVENT_MESSAGE(message_id=8508*)
    → "Are they thinking of bringing their beastmen buddies back here? Next thing you know, they'll be having "Goblin's Day.""
  9: 0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0079 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 11: 0x007E [0x1C] WAIT(60* ticks)
 12: 0x0081 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 13: 0x0083 [0x21] END_EVENT
 14: 0x0084 [0x00] END_REQSTACK()
```
