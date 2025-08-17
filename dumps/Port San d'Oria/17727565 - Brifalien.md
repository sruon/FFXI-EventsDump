# 17727565 - Brifalien

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 144 bytes                 |
| Total Events     | 4                         |
| References Count | 5                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [4](#event-4)            | 0x0001       |      1 |              1 |
| [589](#event-589)        | 0x0002       |     49 |             14 |
| [65535.1](#event-655351) | 0x0033       |     41 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x004B      |          75 |
|       1 | 0x1ED2      |        7890 |
|       2 | 0x001E      |          30 |
|       3 | 0x1ED3      |        7891 |
|       4 | 0x1EDA      |        7898 |

## String References

- **7890**: Hey! Salute when you speak to me! I am second captain of the Royal Knights Youth Division! Don't make me use my nirvana slash on you!
- **7891**: Maybe we could use you. You'd be just a private...but there is plenty of opportunity for advancement.
- **7898**: Yeah, a tradegic stretreat!

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

### Event 589

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 49 bytes |
| Instructions | 14       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       86 00 4D 80 0E 01  1E F0 FF FF 7F 6F 70 5B    ..M........op[
0010: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 1D 01  ..........tlk0..
0020: 80 23 1C 02 80 1D 03 80  23 5E 69 64 6C 30 1C 02  .#......#^idl0..
0030: 80 21 00                                          .!.             
```

#### Opcodes

```
  0: 0x0002 [0x86] Brifalien (ID: 17727565/0x010E804D)->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0008 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x000D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000E [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x000F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=75*
  5: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=7890*)
    → "Hey! Salute when you speak to me! I am second captain of the Royal Knights Youth Division! Don't make me use my nirvana slash on you!"
  6: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0022 [0x1C] WAIT(30* ticks)
  8: 0x0025 [0x1D] PRINT_EVENT_MESSAGE(message_id=7891*)
    → "Maybe we could use you. You'd be just a private...but there is plenty of opportunity for advancement."
  9: 0x0028 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0029 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 11: 0x002E [0x1C] WAIT(30* ticks)
 12: 0x0031 [0x21] END_EVENT
 13: 0x0032 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0033   |
| Data Size    | 41 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:          86 00 4D 80 0E  01 1E F0 FF FF 7F 6F 70     ..M........op
0040: 5B 00 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  [..........tlk0.
0050: 04 80 23 5E 69 64 6C 30  1C 02 80 00              ..#^idl0....    
```

#### Opcodes

```
  0: 0x0033 [0x86] Brifalien (ID: 17727565/0x010E804D)->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0039 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x003E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x003F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0040 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=75*
  5: 0x004F [0x1D] PRINT_EVENT_MESSAGE(message_id=7898*)
    → "Yeah, a tradegic stretreat!"
  6: 0x0052 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0053 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  8: 0x0058 [0x1C] WAIT(30* ticks)
  9: 0x005B [0x00] END_REQSTACK()
```
