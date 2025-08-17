# 16883814 - Geuselibel

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 88 bytes                    |
| Total Events     | 2                           |
| References Count | 4                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [328](#event-328)     | 0x0001       |     47 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2B36      |       11062 |
|       1 | 0x01F1      |         497 |
|       2 | 0x2B37      |       11063 |
|       3 | 0x2B38      |       11064 |

## String References

- **11062**: "The abhorrent one" lives among us... It is because of this that I often fear for the safety of my children and grandchildren...
- **11063**: I can only pray that Altana has mercy on those Tavnazians with pure souls...
- **11064**: ...and strikes down those who bring disaster to our humble city.

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

### Event 328

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 5B 01 80 F8 FF FF   ........#[.....
0010: 7F F8 FF FF 7F 72 65 69  30 1D 02 80 23 1D 03 80  .....rei0...#...
0020: 23 53 F8 FF FF 7F F8 FF  FF 7F 72 65 69 30 21 00  #S........rei0!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=11062*)
    → ""The abhorrent one" lives among us... It is because of this that I often fear for the safety of my children and grandchildren..."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "rei0" with entities [EventEntity, EventEntity], work=497*
  4: 0x0019 [0x1D] PRINT_EVENT_MESSAGE(message_id=11063*)
    → "I can only pray that Altana has mercy on those Tavnazians with pure souls..."
  5: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001D [0x1D] PRINT_EVENT_MESSAGE(message_id=11064*)
    → "...and strikes down those who bring disaster to our humble city."
  7: 0x0020 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0021 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "rei0" with entities [EventEntity, EventEntity]
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```
