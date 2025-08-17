# 16839249 - Steel Bones

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Abyssea - Konschtat (ID: 15) |
| Block Size       | 48 bytes                     |
| Total Events     | 2                            |
| References Count | 2                            |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [289](#event-289)     | 0x0001       |     15 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F83      |        8067 |
|       1 | 0x1F84      |        8068 |

## String References

- **8067**: Abyssean fiends may look like mindless brutes, but they're actually quite adept at adapting to their surroundings. For example, strike down enough of them in a given spot, and you'll soon find their friends coming forth in great numbers.
- **8068**: Makes you wonder who's sending in the order for reinforcements, eh? And those "friends" can get nastier and nastier... I'm speaking from experience here. Leave them alone, and they'll eventually wander off in search of other prey, though.

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

### Event 289

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 21 00   ........#...#!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=8067*)
    → "Abyssean fiends may look like mindless brutes, but they're actually quite adept at adapting to their surroundings. For example, strike down enough of them in a given spot, and you'll soon find their friends coming forth in great numbers."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=8068*)
    → "Makes you wonder who's sending in the order for reinforcements, eh? And those "friends" can get nastier and nastier... I'm speaking from experience here. Leave them alone, and they'll eventually wander off in search of other prey, though."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```
