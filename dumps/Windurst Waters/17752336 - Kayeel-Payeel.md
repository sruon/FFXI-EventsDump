# 17752336 - Kayeel-Payeel

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 80 bytes                  |
| Total Events     | 3                         |
| References Count | 4                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [975](#event-975)     | 0x0001       |     21 |             10 |
| [32693](#event-32693) | 0x0016       |     12 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x3035      |       12341 |
|       1 | 0x3036      |       12342 |
|       2 | 0x3037      |       12343 |
|       3 | 0x3C50      |       15440 |

## String References

- **12341**: Harrumph! The Federation has gone rotten, I tell you. Rotten! Who would have thought the day would come when people would forget the name Kayeel-Payeel, Master Caster of the Aquarian War Warlocks!
- **12342**: If Warlock Warlord Robel-Akbel were only alive today, heads would roll!
- **12343**: How long do the five ministries and the Parliament of Patriarchs plan on keeping his position empty? How long must Fort Karugo-Narugo remain in ruins?
- **15440**: The Starlight Celebration, you say? Hmph. I have no interest in such frivolities...but I'll keep the present anyway.

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

### Event 975

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 21 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    20 01 1E F0 FF FF 7F  1D 00 80 23 1D 01 80 23    .........#...#
0010: 1D 02 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x0001 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0003 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=12341*)
    → "Harrumph! The Federation has gone rotten, I tell you. Rotten! Who would have thought the day would come when people would forget the name Kayeel-Payeel, Master Caster of the Aquarian War Warlocks!"
  3: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x000C [0x1D] PRINT_EVENT_MESSAGE(message_id=12342*)
    → "If Warlock Warlord Robel-Akbel were only alive today, heads would roll!"
  5: 0x000F [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0010 [0x1D] PRINT_EVENT_MESSAGE(message_id=12343*)
    → "How long do the five ministries and the Parliament of Patriarchs plan on keeping his position empty? How long must Fort Karugo-Narugo remain in ruins?"
  7: 0x0013 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0014 [0x21] END_EVENT
  9: 0x0015 [0x00] END_REQSTACK()
```

### Event 32693

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 12 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   42 1E  F0 FF FF 7F 1D 03 80 23        B........#
0020: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0016 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0017 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=15440*)
    → "The Starlight Celebration, you say? Hmph. I have no interest in such frivolities...but I'll keep the present anyway."
  3: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0020 [0x21] END_EVENT
  5: 0x0021 [0x00] END_REQSTACK()
```
