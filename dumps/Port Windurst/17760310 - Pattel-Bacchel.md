# 17760310 - Pattel-Bacchel

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 60 bytes                |
| Total Events     | 2                       |
| References Count | 4                       |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [876](#event-876)     | 0x0001       |     18 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x3EAB      |       16043 |
|       1 | 0x3EAC      |       16044 |
|       2 | 0x3EAD      |       16045 |
|       3 | 0x3EAE      |       16046 |

## String References

- **16043**: Whew! Been fishing up a storm all day, and my eyes are spinning-winning. Why, I couldn't tell a bluetail from a bibikibo in the state I'm in!
- **16044**: Still, I caughtaru twenty fish today. Not bad for a rookie like me, wouldn't you say?
- **16045**: Some of the bigwigs around here say they've caughtaru more than ten times that, but that sounds awful fishy-wishy to me.
- **16046**: Anyway, I'm going to take a breather. Another day (Earth time) or so and I should be fresh as a forest carp. If you ever find yourself pooped after a long day of fishing, I suggestaru you do the same!

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

### Event 876

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 18 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1D 00 80 23 1D 01 80  23 1D 02 80 23 1D 03 80   ...#...#...#...
0010: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0001 [0x1D] PRINT_EVENT_MESSAGE(message_id=16043*)
    → "Whew! Been fishing up a storm all day, and my eyes are spinning-winning. Why, I couldn't tell a bluetail from a bibikibo in the state I'm in!"
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x1D] PRINT_EVENT_MESSAGE(message_id=16044*)
    → "Still, I caughtaru twenty fish today. Not bad for a rookie like me, wouldn't you say?"
  3: 0x0008 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0009 [0x1D] PRINT_EVENT_MESSAGE(message_id=16045*)
    → "Some of the bigwigs around here say they've caughtaru more than ten times that, but that sounds awful fishy-wishy to me."
  5: 0x000C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=16046*)
    → "Anyway, I'm going to take a breather. Another day (Earth time) or so and I should be fresh as a forest carp. If you ever find yourself pooped after a long day of fishing, I suggestaru you do the same!"
  7: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0011 [0x21] END_EVENT
  9: 0x0012 [0x00] END_REQSTACK()
```
