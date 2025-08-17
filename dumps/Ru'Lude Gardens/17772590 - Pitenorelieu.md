# 17772590 - Pitenorelieu

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 112 bytes                 |
| Total Events     | 2                         |
| References Count | 3                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [77](#event-77)       | 0x0001       |     73 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2830      |       10288 |
|       1 | 0x0014      |          20 |
|       2 | 0x2831      |       10289 |

## String References

- **10288**: I get the creeps looking down from the edge. It really hits you how high up we are.
- **10289**: I wonder how they managed to build this place? Jeuno's full of mysteries, like the airships! But the biggest one of all is the archduke. Nobody knows who he is or where he's from.

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

### Event 77

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 73 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 66 01 80 F8   .....op...#f...
0010: FF FF 7F F8 FF FF 7F 74  68 6B 31 1D 02 80 23 53  .......thk1...#S
0020: F8 FF FF 7F F8 FF FF 7F  74 68 6B 31 66 01 80 F8  ........thk1f...
0030: FF FF 7F F8 FF FF 7F 74  68 6B 32 53 F8 FF FF 7F  .......thk2S....
0040: F8 FF FF 7F 74 68 6B 32  21 00                    ....thk2!.      
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=10288*)
    → "I get the creeps looking down from the edge. It really hits you how high up we are."
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=10289*)
    → "I wonder how they managed to build this place? Jeuno's full of mysteries, like the airships! But the biggest one of all is the archduke. Nobody knows who he is or where he's from."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  9: 0x002C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
 10: 0x003B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
 11: 0x0048 [0x21] END_EVENT
 12: 0x0049 [0x00] END_REQSTACK()
```
