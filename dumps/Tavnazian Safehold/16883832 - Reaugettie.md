# 16883832 - Reaugettie

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Tavnazian Safehold (ID: 26) |
| Block Size       | 88 bytes                    |
| Total Events     | 3                           |
| References Count | 4                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [391](#event-391)     | 0x0001       |     11 |              5 |
| [392](#event-392)     | 0x000C       |     30 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2B7A      |       11130 |
|       1 | 0x2B7B      |       11131 |
|       2 | 0x0027      |          39 |
|       3 | 0x2B7C      |       11132 |

## String References

- **11130**: This is the entrance to the Tavnazian Safehold.
- **11131**: Twenty years ago, we were all overjoyed when news of the allied forces' victory over the Shadow Lord's armies finally reached our island.
- **11132**: However, deep inside we knew that this would only be a short-lived triumph. As long as there is light in the world, there will always exist darkness.

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

### Event 391

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 21 00               ........#!.    
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=11130*)
    → "This is the entrance to the Tavnazian Safehold."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x21] END_EVENT
  4: 0x000B [0x00] END_REQSTACK()
```

### Event 392

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      1E F0 FF FF              ....
0010: 7F 1D 01 80 23 66 02 80  F8 FF FF 7F F8 FF FF 7F  ....#f..........
0020: 74 6C 6B 30 1D 03 80 23  21 00                    tlk0...#!.      
```

#### Opcodes

```
  0: 0x000C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=11131*)
    → "Twenty years ago, we were all overjoyed when news of the allied forces' victory over the Shadow Lord's armies finally reached our island."
  2: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0015 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=39*
  4: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=11132*)
    → "However, deep inside we knew that this would only be a short-lived triumph. As long as there is light in the world, there will always exist darkness."
  5: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0028 [0x21] END_EVENT
  7: 0x0029 [0x00] END_REQSTACK()
```
