# 17727543 - Noquerelle

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Port San d'Oria (ID: 232) |
| Block Size       | 80 bytes                  |
| Total Events     | 2                         |
| References Count | 3                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [583](#event-583)     | 0x0001       |     43 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x1DE3      |        7651 |
|       2 | 0x1DE4      |        7652 |

## String References

- **7651**: Below these stairs lies the auction house. Some may grumble about proud San d'Orians reduced to squabbling merchants, but I care not.
- **7652**: In fact, I agree with Prince Pieuje. The Kingdom must welcome change, before the rest of the world passes her by.

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

### Event 583

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 43 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1C 00 80 1D 02  ...tlk0...#.....
0020: 80 23 5E 69 64 6C 30 1C  00 80 21 00              .#^idl0...!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=30*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=7651*)
    → "Below these stairs lies the auction house. Some may grumble about proud San d'Orians reduced to squabbling merchants, but I care not."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1C] WAIT(30* ticks)
  7: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=7652*)
    → "In fact, I agree with Prince Pieuje. The Kingdom must welcome change, before the rest of the world passes her by."
  8: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0022 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 10: 0x0027 [0x1C] WAIT(30* ticks)
 11: 0x002A [0x21] END_EVENT
 12: 0x002B [0x00] END_REQSTACK()
```
